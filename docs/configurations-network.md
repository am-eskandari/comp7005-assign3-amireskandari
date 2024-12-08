# **Port Scanner Configuration Testing Document (Lab Network)**

This document lists all configurations required based on the assignment instructions, along with the respective commands
to test the program’s functionality and ensure it works logically.

I'm running these demos on:

```bash
192.168.0.10
```

Double Check the open and closed ports with `nmap`:

```bash
sudo nmap -p 1-1000 192.168.0.10
```

---

## **1. Basic Functionality**

### **Default Scan (All Ports: 1–65535)**

**Description**: Scans all ports on a target machine when no port range is provided.  
**Command**:

```bash
sudo python3 port_scanner.py 192.168.0.10
```

**Cross-reference**:

```bash
sudo nmap -p 1-65535 192.168.0.10
```

---

### **Single Port Scan**

**Description**: Scans a specific port using the `--start` and `--end` arguments with the same value.  
**Command**:

```bash
sudo python3 port_scanner.py 192.168.0.10 --start 22 --end 22
```

**Cross-reference**:

```bash
sudo nmap -p 22 192.168.0.10
```

---

### **Range of Ports Scan**

#### **1. Small Range**

**Description**: Scans a small range of ports using the `--start` and `--end` arguments.  
**Command**:

```bash
sudo python3 port_scanner.py 192.168.0.10 --start 20 --end 30
```

**Cross-reference**:

```bash
sudo nmap -p 20-30 192.168.0.10
```

#### **2. Medium Range**

**Description**: Scans a medium range of ports (e.g., ports 50–200).  
**Command**:

```bash
sudo python3 port_scanner.py 192.168.0.10 --start 50 --end 200
```

**Cross-reference**:

```bash
sudo nmap -p 50-200 192.168.0.10
```

---

### **Delay Between Scans**

**Description**: Adds a delay (in milliseconds) between scans using the `--delay` argument.  
**Command**:

```bash
sudo python3 port_scanner.py 192.168.0.10 --start 20 --end 80 --delay 50
```

**Cross-reference**:

```bash
sudo nmap -p 20-80 192.168.0.10
```

---

### **Start Port Only**

**Description**: Scans from a specific start port to port 65535.  
**Command**:

```bash
sudo python3 port_scanner.py 192.168.0.10 --start 55000
```

**Cross-reference**:

```bash
sudo nmap -p 55000-65535 192.168.0.10
```

---

### **End Port Only**

**Description**: Scans from port 1 to a specific end port.  
**Command**:

```bash
sudo python3 port_scanner.py 192.168.0.10 --end 1500
```

**Cross-reference**:

```bash
sudo nmap -p 1-1500 192.168.0.10
```

---

## **2. Real-World Scenarios**

### **Testing Denied Ports**

**Description**: Scans well-known restricted ports (e.g., 1–25) to confirm proper detection of closed or filtered
states.  
**Command**:

```bash
sudo python3 port_scanner.py 192.168.0.10 --start 1 --end 25
```

**Cross-reference**:

```bash
sudo nmap -p 1-25 192.168.0.10
```

---

### **Localhost Open Port**

**Description**: Confirms detection of an open port on the localhost (e.g., SSH on port 22).  
**Command**:

```bash
sudo python3 port_scanner.py 192.168.0.10 --start 22 --end 22
```

**Cross-reference**:

```bash
sudo nmap -p 22 192.168.0.10
```

---

## **3. Validation of Error Handling**

### **Invalid IP Address**

**Description**: Ensures the program correctly handles invalid IP addresses.  
**Command**:

```bash
sudo python3 port_scanner.py 999.999.999.999
```

---

### **Reversed Port Range**

**Description**: Validates that the program detects and reports an invalid port range where the start port is greater
than the end port.  
**Command**:

```bash
sudo python3 port_scanner.py 192.168.0.10 --start 100 --end 50
```

---

### **Negative Port Range**

**Description**: Verifies that negative port values are rejected.  
**Command**:

```bash
sudo python3 port_scanner.py 192.168.0.10 --start -10 --end 50
```

---

### **Exceeding Maximum Port Range**

**Description**: Ensures ports outside the valid range of 1–65535 are handled gracefully.  
**Command**:

```bash
sudo python3 port_scanner.py 192.168.0.10 --start 1 --end 70000
```

---

### **Non-Integer Port Values**

**Description**: Validates handling of non-integer values for ports.  
**Command**:

```bash
sudo python3 port_scanner.py 192.168.0.10 --start abc --end 80
```

---

### **Invalid Delay**

**Description**: Tests the handling of non-integer or negative values for the delay.  
**Command**:

```bash
sudo python3 port_scanner.py 192.168.0.10 --start 22 --end 22 --delay xyz
```