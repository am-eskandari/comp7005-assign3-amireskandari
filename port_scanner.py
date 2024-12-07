import argparse
import socket
import time

from scapy.all import IP, TCP, sr1


class PortScanner:
    def __init__(self, target, start_port=1, end_port=65535, delay=0):
        self.target = target
        self.start_port = start_port
        self.end_port = end_port
        self.delay = delay / 1000  # Convert milliseconds to seconds
        self.results = []

    def validate_inputs(self):
        """Validate the target IP and port range."""
        try:
            socket.inet_aton(self.target)  # Check valid IP address
        except socket.error:
            raise ValueError("Invalid IP address.")

        if not (1 <= self.start_port <= 65535 and 1 <= self.end_port <= 65535):
            raise ValueError("Port range must be between 1 and 65535.")
        if self.start_port > self.end_port:
            raise ValueError("Start port cannot be greater than end port.")

    def scan_port(self, port):
        """Send SYN packet to the target port and interpret the response."""
        packet = IP(dst=self.target) / TCP(dport=port, flags="S")
        response = sr1(packet, timeout=1, verbose=0)

        if response is None:
            return "Filtered"
        elif response.haslayer(TCP):
            if response[TCP].flags == "SA":  # SYN-ACK
                return "Open"
            elif response[TCP].flags == "RA":  # RST-ACK
                return "Closed"
        return "Unknown"

    def perform_scan(self):
        """Scan the range of ports and collect results."""
        for port in range(self.start_port, self.end_port + 1):
            try:
                status = self.scan_port(port)
                self.results.append((port, status))
                print(f"Port {port}: {status}")
                time.sleep(self.delay)  # Add delay between scans
            except Exception as e:
                print(f"Error scanning port {port}: {e}")

    def output_results(self):
        """Print the scan results."""
        print("\nScan Results:")
        for port, status in self.results:
            print(f"Port {port}: {status}")


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
        scanner.perform_scan()
        scanner.output_results()
    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
