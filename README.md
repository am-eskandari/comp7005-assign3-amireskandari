# Port Scanner Using Scapy

## Overview

This project implements a basic port scanner using the **Scapy** library in Python. The scanner mimics the behavior of *
*hping3** and is designed to determine the status of TCP ports (open, closed, or filtered) on a specified target
machine. This tool is developed as part of the Network Security course (COMP 7005) and adheres to the assignment
guidelines.

## Features

- **TCP SYN Scanning**: Determines the status of ports using crafted SYN packets.
- **Customizable Port Range**: Scan a single port, a range, or all ports from 1 to 65535.
- **Default Behavior**: Automatically scans all ports (1–65535) if no range is specified.
- **Optional Delay**: Introduces a delay between scans to avoid overwhelming the target.
- **Command-Line Interface**: Accepts target IP, port range, and delay as arguments.
- **Graceful Error Handling**: Provides descriptive error messages for invalid inputs or unreachable hosts.

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

Run the script using the following commands:

```bash
sudo python3 port_scanner.py <target_ip> [--start <start_port>] [--end <end_port>] [--delay <delay_in_ms>]
```

#### Arguments

- `<target_ip>`: Required. The IP address of the machine to scan.
- `--start <start_port>`: Optional. The starting port for the scan (default: 1).
- `--end <end_port>`: Optional. The ending port for the scan (default: 65535).
- `--delay <delay_in_ms>`: Optional. Delay in milliseconds between each port scan.

#### Examples

To scan all ports on a target machine:

```bash
sudo python3 port_scanner.py 192.168.1.10
```

To scan ports 20-80 with a 100 ms delay:

```bash
sudo python3 port_scanner.py 192.168.1.10 --start 20 --end 80 --delay 100
```

### Running Tests with PyTest

To validate the program’s behavior and ensure all functionality works as expected, run the PyTest suite:

1. Install `pytest`:
   ```bash
   pip install pytest
   ```

2. Navigate to the `tests/` directory and execute the following command:
   ```bash
   sudo pytest -s tests_cli.py
   ```

3. Review the test results in the terminal to ensure all cases pass.

---

## Error Handling

- **Invalid IP Addresses**: Invalid IP addresses trigger descriptive error messages.
- **Unreachable Hosts**: Provides clear feedback if the host is unreachable.
- **Improper Arguments**: Usage instructions are displayed for missing or incorrect arguments.
- **Network Errors**: Timeouts or other network issues are logged and handled gracefully.

For more details, refer to the following resources:

- [PyTests](https://github.com/am-eskandari/comp7005-assign3-amireskandari/blob/main/tests/tests_cli.py) for CLI test
  cases.
- [Configurations](https://github.com/am-eskandari/comp7005-assign3-amireskandari/blob/main/docs/configurations.md) for
  parameter usage examples.

## Constraints

- Must be executed on a UNIX-based operating system. (Tested on, Arch Linux, Manjaro, Kali Linux)
- Requires elevated privileges (`sudo`).

## Known Limitations

- Scans might take longer for a large range of ports if delays are specified.
- Results accuracy depends on the network environment and firewall rules.

## Resources

- [Scapy Documentation](https://scapy.net/doc/)
- [Python 3.x Documentation](https://www.python.org/)

## License

This project is for educational purposes and adheres to the guidelines provided for BCIT and COMP 7005.

---
