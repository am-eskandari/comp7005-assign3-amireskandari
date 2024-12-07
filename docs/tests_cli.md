### **CLI Argument Test Cases for `port_scanner.py`**

This document outlines the test cases for validating the behavior of the `port_scanner.py` program when handling various
CLI arguments. The tests are designed to ensure proper functionality, error handling, and robustness of the program.

---

#### **Valid Input Scenarios**

| **Test Case**                          | **Description**                                                                                          | **Expected Outcome**                                                 |
|----------------------------------------|----------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------|
| **Valid Input: Single Port**           | Provide a valid target IP with the same value for start and end ports.                                   | Program scans the single port and outputs its result.                |
| **Valid Input: Range of Denied Ports** | Provide a range of low-numbered ports (e.g., `--start 1 --end 25`) where access is typically restricted. | Program identifies ports as closed or filtered due to denied access. |
| **Valid Input: Delay Included**        | Provide valid target IP, port range, and delay in milliseconds.                                          | Program scans ports with the specified delay between each scan.      |

---

#### **Invalid Input Scenarios**

| **Test Case**                          | **Description**                                                                 | **Expected Outcome**                                                                    |
|----------------------------------------|---------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| **Invalid IP Address**                 | Provide an invalid IP address (e.g., `999.999.999.999`).                        | Program outputs an error message indicating invalid IP and exits gracefully.            |
| **Invalid Port Range: Negative Ports** | Provide a negative value for start or end ports (e.g., `--start -10 --end 50`). | Program outputs an error message indicating invalid port range.                         |
| **Invalid Port Range: Exceeding Max**  | Provide a port range exceeding 65535 (e.g., `--start 1 --end 70000`).           | Program outputs an error message indicating invalid port range.                         |
| **Invalid Port Range: Reversed**       | Provide a start port greater than the end port (e.g., `--start 100 --end 50`).  | Program outputs an error message indicating start port cannot be greater than end port. |
| **Invalid Delay: Negative Value**      | Provide a negative value for delay (e.g., `--delay -100`).                      | Program outputs an error message indicating delay must be non-negative.                 |

---

#### **Wrong Argument Types**

| **Test Case**                              | **Description**                                                                           | **Expected Outcome**                                                      |
|--------------------------------------------|-------------------------------------------------------------------------------------------|---------------------------------------------------------------------------|
| **Wrong Argument Type: Non-integer Ports** | Provide a non-integer value for ports (e.g., `--start abc --end 80`).                     | Program outputs an error message: "Port range must be an integer."        |
| **Wrong Argument Type: Non-integer Delay** | Provide a non-integer value for delay (e.g., `--delay xyz`).                              | Program outputs an error message: "Delay must be a non-negative integer." |
| **Wrong Argument Type: Non-IP Target**     | Provide a string that isn’t a valid IP address (e.g., `python3 port_scanner.py abc.def`). | Program outputs an error message: "Invalid IP address."                   |

---

#### **Missing or Unexpected Arguments**

| **Test Case**                               | **Description**                                                                                 | **Expected Outcome**                                                                    |
|---------------------------------------------|-------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------|
| **Missing Required Argument: Target IP**    | Omit the target IP address (e.g., `--start 20 --end 80 --delay 100`).                           | Program outputs an error message: "Target IP is required."                              |
| **Missing Required Parameters: Port Range** | Omit start or end values after providing the `--start` or `--end` flag (e.g., `--start --end`). | Program outputs an error message: "Port range must include valid start and end values." |
| **Unexpected Additional Argument**          | Provide an extra, unsupported argument (e.g., `--foo 123`).                                     | Program outputs an error message: "Unrecognized argument '--foo'."                      |
| **No Arguments at All**                     | Run the program with no arguments (e.g., `python3 port_scanner.py`).                            | Program outputs usage instructions or help message.                                     |

---

#### **Help and Usage**

| **Test Case**    | **Description**                         | **Expected Outcome**                          |
|------------------|-----------------------------------------|-----------------------------------------------|
| **Help Command** | Run the program with the `--help` flag. | Program displays usage information and exits. |

---

### **Notes**

1. **Excluded Tests for Full Port Range**:
    - Testing the full range (`1–65535`) is excluded due to time constraints. Smaller port ranges sufficiently validate
      the scanning logic.

2. **Testing Denied Access Ports**:
    - Testing ports in the range `1–1023` ensures the program correctly identifies closed or filtered ports, which are
      often restricted.