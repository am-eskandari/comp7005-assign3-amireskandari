# Summary of the Assignment

## **Objective**
- Build a Python-based **port scanner** using **Scapy**, mimicking the behavior of **hping3**.
- Develop skills in:
  - TCP/IP protocol handling.
  - Packet crafting and response analysis.
  - Command-line argument management.

## **Learning Outcomes**
By completing this assignment, students will:
- Understand port scanning techniques and mechanics.
- Use Scapy to create and send custom TCP packets.
- Implement **SYN scanning** to assess port statuses.
- Manage command-line arguments with optional features.

## **Assignment Requirements**
- Write a Python program using Scapy to:
  - Perform **TCP SYN scans** on specified ports of a target machine.
  - Determine port statuses: **open**, **closed**, or **filtered**.
- Provide **command-line arguments** for:
  - **Target IP Address:** Mandatory.
  - **Port Range:** Defaults to 1-65535, with flexibility for start/end.
  - **Optional Delay:** Specify delays between scans (in milliseconds).

## **How Port Scanning Works**
- **TCP SYN Scanning:** 
  - **Open Port:** Receives SYN-ACK.
  - **Closed Port:** Receives RST.
  - **Filtered Port:** No response or ICMP unreachable.

## **Constraints**
- Must run on **UNIX-based systems** (Linux, FreeBSD, macOS).
- Utilize **Scapy** for packet crafting.
- Handle errors gracefully, including invalid IPs and unreachable hosts.
- Provide meaningful command-line feedback for incorrect inputs.

## **Hints**
- Start testing with a small port range on a local machine.
- Use a controlled setup for external scans.
- Run with elevated privileges (e.g., `sudo`) for Scapy to send raw packets.
- Convert milliseconds to seconds for delay management.
- Look for specific TCP flags in responses.