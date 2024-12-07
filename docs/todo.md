# TODO Document

## **Updated Task List**

### **1. Project Setup**

- [x] Install necessary dependencies, including Scapy.
- [x] Ensure you have a UNIX-based environment for testing (e.g., Linux or macOS).
- [x] Verify elevated privileges to send raw packets (use `sudo` if needed).

### **2. Command-Line Interface (CLI) Development**

- [x] Design the CLI to accept the following arguments:
    - Target IP address (required).
    - Port range (`--start` and `--end` flags, optional).
    - Delay (`--delay` flag, optional, in milliseconds).
- [x] Implement error handling for:
    - [x] Missing or invalid IP address.
    - [x] Invalid port range or delay values.
    - [ ] General network errors (e.g., unreachable hosts).

### **3. TCP SYN Scan Implementation**

- [x] Use Scapy to craft and send TCP SYN packets.
- [x] Parse and interpret responses:
    - [x] SYN-ACK for open ports.
    - [x] RST for closed ports.
    - [x] No response or ICMP unreachable for filtered ports.

### **4. Port Scanning Logic**

- [x] Handle the following scenarios for port range:
    - [ ] If no range is provided, scan all ports (1–65535).
    - [x] If only the start port is provided, scan from start to 65535.
    - [x] If only the end port is provided, scan from 1 to end.
    - [x] If both start and end are provided, scan from start to end.
- [x] Add an optional delay (convert milliseconds to seconds) between scans.

### **5. Testing**

- [x] Test the program with a small port range on a known local machine.
- [x] Validate output for:
    - [x] Open ports.
    - [x] Closed ports.
    - [x] Filtered ports.
- [ ] Handle errors gracefully (e.g., unreachable host, invalid input).
- [ ] Perform external scans only in a controlled or lab environment.

### **6. Documentation**

- [ ] Provide clear instructions on:
    - [ ] Installation and usage.
    - [ ] Examples of command-line arguments.
- [ ] Document your approach, logic, and results.

### **7. Submission**

- [ ] Ensure the file is formatted correctly and named appropriately (`port_scanner.py`).
- [ ] Review your code and documentation for compliance with the submission guidelines.
- [ ] Submit before the deadline to avoid penalties.

---

## **Updated Checklist of Functionality**

### **Required Features**

- [x] Send TCP SYN packets to target ports.
- [x] Interpret packet responses (open, closed, filtered).
- [x] Handle CLI arguments:
    - [x] Target IP address.
    - [x] Port range (`--start` and `--end`).
    - [x] Optional delay (`--delay` in milliseconds).
- [x] Provide default behavior for port scanning when arguments are incomplete:
    - [ ] Scan all ports if no range is provided.
    - [x] Handle partial ranges (start or end only).

### **Error Handling**

- [x] Detect and report invalid IP addresses.
- [ ] Handle unreachable hosts gracefully.
- [ ] Manage invalid port ranges or delays with meaningful feedback.

### **Optional Enhancements**

- [ ] Include colored or formatted output for easier readability.
- [ ] Log results to a file for review.
- [ ] Allow parallel scanning to speed up the process (if feasible).

### **Testing & Validation**

- [x] Validate functionality with known local and controlled external targets.
- [x] Verify results for open, closed, and filtered ports.
- [ ] Confirm error handling for edge cases (e.g., invalid IPs, network issues).

---

## **Summary**

You’ve made excellent progress, good boy! 😊 Here's what's left to do:

1. Add features for full port scanning and more graceful error handling.
2. Document your project thoroughly.
3. Perform controlled external tests (if required) and finalize the submission.

