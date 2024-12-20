import argparse
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

from scapy.all import IP, TCP, sr1
from tqdm import tqdm

from utils.logger import setup_logger
from utils.pretty_print import display_error, display_results, display_info
from utils.validation import validate_ip, validate_port_range, validate_delay


class PortScanner:
    def __init__(
        self,
        target,
        start_port=1,
        end_port=65535,
        delay=0,
        log_file="log_scan_results.log",
        max_threads=48,
    ):
        self.target = target
        self.start_port = start_port
        self.end_port = end_port
        self.delay = delay / 1000  # Convert milliseconds to seconds
        self.results = []
        self.logger = setup_logger(log_file)  # Initialize the logger
        self.max_threads = max_threads  # Maximum number of threads

    def validate_inputs(self):
        """Validate the target IP and port range."""
        self.logger.info("Validating inputs...")
        validate_ip(self.target)
        validate_port_range(self.start_port, self.end_port)
        validate_delay(self.delay)
        self.logger.info("Inputs validated successfully.")

    def scan_port(self, port):
        """Send SYN packet to the target port and interpret the response."""
        packet = IP(dst=self.target) / TCP(dport=port, flags="S")
        response = sr1(packet, timeout=1, verbose=0)

        if response is None:
            return port, "Filtered"
        elif response.haslayer(TCP):
            if response[TCP].flags == "SA":  # SYN-ACK
                return port, "Open"
            elif response[TCP].flags == "RA":  # RST-ACK
                return port, "Closed"
        return port, "Unknown"

    def perform_scan(self):
        """Scan the range of ports concurrently and collect results."""
        total_ports = self.end_port - self.start_port + 1
        self.logger.info(
            f"Starting scan on {self.target} from port {self.start_port} to {self.end_port} with {self.max_threads} threads..."
        )
        display_info(
            f"ℹ️ Starting scan on {self.target} from port {self.start_port} to {self.end_port} with {self.max_threads} threads..."
        )

        start_time = time.time()  # Record the start time

        # Create a progress bar
        with tqdm(
            total=total_ports, desc="Scanning Ports", unit="port"
        ) as progress_bar:
            with ThreadPoolExecutor(max_workers=self.max_threads) as executor:
                futures = {
                    executor.submit(self.scan_port, port): port
                    for port in range(self.start_port, self.end_port + 1)
                }

                for future in as_completed(futures):
                    try:
                        port, status = future.result()
                        self.results.append((port, status))
                        self.logger.info(f"Port {port}: {status}")
                    except Exception as e:
                        self.logger.error(f"Error scanning port: {e}")
                    finally:
                        progress_bar.update(1)  # Update the progress bar

        end_time = time.time()  # Record the end time
        elapsed_time_ms = (
            end_time - start_time
        ) * 1000  # Calculate the elapsed time in milliseconds
        display_info(
            f"✅ Scan completed in {elapsed_time_ms:.2f} milliseconds."
        )  # Display the time taken
        self.logger.info(f"Scan completed in {elapsed_time_ms:.2f} milliseconds.")

    def output_results(self):
        """Display the scan results, log them, and show totals."""
        # Count the status of ports
        total_open = sum(1 for _, status in self.results if status == "Open")
        total_closed = sum(1 for _, status in self.results if status == "Closed")
        total_filtered = sum(1 for _, status in self.results if status == "Filtered")

        # Pretty print results
        display_results(sorted(self.results))  # Sort results by port for readability

        # Display totals
        display_info(
            f"🔢 Totals: Open: {total_open}, Closed: {total_closed}, Filtered: {total_filtered}"
        )
        self.logger.info(
            f"Totals: Open: {total_open}, Closed: {total_closed}, Filtered: {total_filtered}"
        )

        # Log results
        self.logger.info("Scan completed. Results:")
        for port, status in sorted(self.results):
            self.logger.info(f"Port {port}: {status}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="TCP SYN Port Scanner")
    parser.add_argument("target", help="Target IP address")
    parser.add_argument("--start", type=int, default=1, help="Start port")
    parser.add_argument("--end", type=int, default=65535, help="End port")
    parser.add_argument("--delay", type=int, default=0, help="Delay in milliseconds")
    args = parser.parse_args()

    try:
        scanner = PortScanner(args.target, args.start, args.end, args.delay)
        scanner.validate_inputs()
        display_info("✅ Valid input detected. Starting scan...")
        scanner.perform_scan()
        scanner.output_results()
    except ValueError as e:
        display_error(e)
    except KeyboardInterrupt:
        display_error("❌ Scan interrupted by user. Ports scanned so far are logged.")
    except Exception as e:
        display_error(f"Unexpected error: {e}")
