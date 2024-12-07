Certainly! Here's a breakdown of the **tasks** and a **checklist of functionality** for your network security class
project:

---

### **Task List**

#### **1. Project Setup**

- [ ] Install necessary dependencies, including Scapy.
- [ ] Ensure you have a UNIX-based environment for testing (e.g., Linux or macOS).
- [ ] Verify elevated privileges to send raw packets (use `sudo` if needed).

#### **2. Command-Line Interface (CLI) Development**

- [ ] Design the CLI to accept the following arguments:
    - Target IP address (required).
    - Port range (`--start` and `--end` flags, optional).
    - Delay (`--delay` flag, optional, in milliseconds).
- [ ] Implement error handling for:
    - Missing or invalid IP address.
    - Invalid port range or delay values.
    - General network errors.

#### **3. TCP SYN Scan Implementation**

- [ ] Use Scapy to craft and send TCP SYN packets.
- [ ] Parse and interpret responses:
    - SYN-ACK for open ports.
    - RST for closed ports.
    - No response or ICMP unreachable for filtered ports.

#### **4. Port Scanning Logic**

- [ ] Handle the following scenarios for port range:
    - If no range is provided, scan all ports (1–65535).
    - If only the start port is provided, scan from start to 65535.
    - If only the end port is provided, scan from 1 to end.
    - If both start and end are provided, scan from start to end.
- [ ] Add an optional delay (convert milliseconds to seconds) between scans.

#### **5. Testing**

- [ ] Test the program with a small port range on a known local machine.
- [ ] Validate output for:
    - Open ports.
    - Closed ports.
    - Filtered ports.
- [ ] Handle errors gracefully (e.g., unreachable host, invalid input).
- [ ] Perform external scans only in a controlled or lab environment.

#### **6. Documentation**

- [ ] Provide clear instructions on:
    - Installation and usage.
    - Examples of command-line arguments.
- [ ] Document your approach, logic, and results.

#### **7. Submission**

- [ ] Ensure the file is formatted correctly and named appropriately (`port_scanner.py`).
- [ ] Review your code and documentation for compliance with the submission guidelines.
- [ ] Submit before the deadline to avoid penalties.

---

### **Checklist of Functionality**

#### **Required Features**

- [ ] Send TCP SYN packets to target ports.
- [ ] Interpret packet responses (open, closed, filtered).
- [ ] Handle CLI arguments:
    - [ ] Target IP address.
    - [ ] Port range (`--start` and `--end`).
    - [ ] Optional delay (`--delay` in milliseconds).
- [ ] Provide default behavior for port scanning when arguments are incomplete:
    - Scan all ports if no range is provided.
    - Handle partial ranges (start or end only).

#### **Error Handling**

- [ ] Detect and report invalid IP addresses.
- [ ] Handle unreachable hosts gracefully.
- [ ] Manage invalid port ranges or delays with meaningful feedback.

#### **Optional Enhancements**

- [ ] Include colored or formatted output for easier readability.
- [ ] Log results to a file for review.
- [ ] Allow parallel scanning to speed up the process (if feasible).

#### **Testing & Validation**

- [ ] Validate functionality with known local and controlled external targets.
- [ ] Verify results for open, closed, and filtered ports.
- [ ] Confirm error handling for edge cases (e.g., invalid IPs, network issues).

---

