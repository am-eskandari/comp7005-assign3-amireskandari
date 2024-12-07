# Tips for using venv and linux

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

