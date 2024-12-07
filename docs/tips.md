# Tips for using venv, Python and linux

---

## Python Virtual Environment Guide (Arch Linux + Bash)

This guide explains how to manage a Python virtual environment (`venv`) on Arch Linux using Bash.

### Activating the Virtual Environment

To enter the virtual environment, use:  
`source myenv/bin/activate`

### Deactivating the Virtual Environment

To exit the virtual environment, use:  
`deactivate`

### Installing Packages

Ensure the virtual environment is activated before running these commands:

- Install a package:  
  `pip install <package_name>`

- Install packages from a `requirements.txt` file:  
  `pip install -r requirements.txt`

### Saving Installed Packages

Save your environment's packages into a `requirements.txt` file:  
`pip freeze > requirements.txt`

### Checking Python and Package Versions

- Check Python version:  
  `python --version`

- Check installed packages:  
  `pip list`

---

## **Creating a Clean Project Tree Output on Arch Linux**

### **Step 1: Install the `tree` Command**

Ensure the `tree` utility is installed. On Arch Linux, use `pacman`:

```bash
sudo pacman -S tree
```

### **Step 2: Generate the Tree Output**

Navigate to your project directory:

```bash
cd /path/to/your/project
```

Run the following `tree` command to create a clean and focused output:

```bash
tree -I "__pycache__|*.pyc|*.log|node_modules" --prune -L 3 >   repo-structure.txt
```

- **Options Explained:**
    - `-I`: Exclude files/directories that match patterns (e.g., `__pycache__`, `*.pyc`, logs).
    - `--prune`: Hides empty directories that match the excluded patterns.
    - `-L 3`: Limits the depth of the tree to 3 levels for brevity.
    - `>   repo-structure.txt`: Saves the output to a file for sharing or documentation.

### **Step 3: Review the Output**

Open the generated `  repo-structure.txt` file to verify:

```bash
cat   repo-structure.txt
```

### **Step 4: Customize for Specific Needs**

Modify the command to suit your project's structure:

- To exclude virtual environments:
  ```bash
  tree -I "myenv|__pycache__|*.pyc" --prune -L 3
  ```
- To display more levels:
  ```bash
  tree -L 5
  ```
- To directly print the output in the terminal without saving:
  ```bash
  tree -I "__pycache__|*.pyc|node_modules" --prune
  ```

### **Step 5: Add It to Your Documentation**

Copy-paste the output of `  repo-structure.txt` into your `README.md` or documentation under a "Project Structure"
section.

---

## **Example Workflow on Arch**

1. Navigate to your project directory:
   ```bash
   cd ~/my_project
   ```
2. Run a clean tree command:
   ```bash
   tree -I "__pycache__|*.pyc|*.log|node_modules" --prune -L 3 >   repo-structure.txt
   ```
3. Verify the output:
   ```bash
   cat   repo-structure.txt
   ```
4. Add the content of `repo-structure.txt` to your documentation.

---

