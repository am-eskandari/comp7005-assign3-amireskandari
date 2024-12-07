class PortScannerCLI:
    @staticmethod
    def parse_arguments():
        """Parses and validates command-line arguments."""
        parser = argparse.ArgumentParser(description="TCP SYN Port Scanner using Scapy")
        parser.add_argument("target", help="Target IP address to scan")
        parser.add_argument("--start", type=int, default=1, help="Start of the port range (default: 1)")
        parser.add_argument("--end", type=int, default=65535, help="End of the port range (default: 65535)")
        parser.add_argument("--delay", type=int, default=0, help="Delay between scans in milliseconds (default: 0)")
        args = parser.parse_args()

        # Validate port range
        if args.start < 1 or args.end > 65535 or args.start > args.end:
            parser.error("Invalid port range. Start and end ports must be between 1 and 65535, and start <= end.")
        
        return args

    @staticmethod
    def run():
        """Main method to run the port scanner."""
        args = PortScannerCLI.parse_arguments()

        try:
            scanner = PortScanner(
                target_ip=args.target,
                start_port=args.start,
                end_port=args.end,
                delay=args.delay
            )
            scanner.perform_scan()
        except PermissionError:
            print("Error: This script requires elevated privileges. Run with sudo.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    PortScannerCLI.run()
