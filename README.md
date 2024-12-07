# Port Scanner Using Scapy

## Overview

This project implements a basic port scanner using the **Scapy** library in Python. The scanner mimics the behavior of **hping3** and is designed to determine the status of TCP ports (open, closed, or filtered) on a specified target machine. This tool is developed as part of the Network Security course (COMP 7005) and adheres to the assignment guidelines.

## Features

- **TCP SYN Scanning**: Determines the status of ports using crafted SYN packets.
- **Customizable Port Range**: Scan a single port, a range, or all ports from 1 to 65535.
- **Optional Delay**: Introduces a delay between scans to avoid overwhelming the target.
- **Command-Line Interface**: Accepts target IP, port range, and delay as arguments.

## How It Works

The scanner sends TCP SYN packets to specified ports and interprets the responses:
- **Open Port**: The target responds with a SYN-ACK packet.
- **Closed Port**: The target responds with an RST packet.
- **Filtered Port**: No response or an ICMP unreachable message is received.

This scanning technique is commonly used for reconnaissance because it doesn’t fully establish a TCP connection.

## Usage

### Prerequisites

1. Python 3.x installed on a UNIX-based operating system (e.g., Linux, macOS).
2. Install the Scapy library using the following command:
   ```bash
   pip install scapy
   ```
3. Elevated privileges (use `sudo`).

### Running the Scanner

Run the script using the following command:
```bash
python3 port_scanner.py <target_ip> [--start <start_port>] [--end <end_port>] [--delay <delay_in_ms>]
```

#### Arguments

- `<target_ip>`: Required. The IP address of the machine to scan.
- `--start <start_port>`: Optional. The starting port for the scan (default: 1).
- `--end <end_port>`: Optional. The ending port for the scan (default: 65535).
- `--delay <delay_in_ms>`: Optional. Delay in milliseconds between each port scan.

#### Examples

To scan all ports on a target machine:
```bash
python3 port_scanner.py 192.168.1.10
```

To scan ports 20-80 with a 100 ms delay:
```bash
python3 port_scanner.py 192.168.1.10 --start 20 --end 80 --delay 100
```

## Error Handling

- Invalid IP addresses or unreachable hosts are gracefully handled with descriptive error messages.
- Improper arguments trigger usage instructions.

## Testing

- Test the scanner with a small port range on a known local machine for validation.
- For external scans, use a controlled environment or a lab setup.

## Learning Outcomes

By completing this project, you will:
- Understand the mechanics of port scanning and TCP/IP protocols.
- Gain experience crafting and sending custom packets with Scapy.
- Develop skills in handling command-line arguments and implementing optional features.

## Constraints

- Must be executed on a UNIX-based operating system.
- Requires elevated privileges (`sudo`).

## Resources

- [Scapy Documentation](https://scapy.net/doc/)
- [Python 3.x Documentation](https://www.python.org/)

## License

This project is for educational purposes and adheres to the guidelines provided for BCIT and COMP 7005.