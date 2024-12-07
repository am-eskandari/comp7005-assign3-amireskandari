import os
import subprocess


def run_cli(args):
    """Helper function to run the port_scanner.py script with given args."""
    script_path = os.path.abspath(
        os.path.join(os.path.dirname(__file__), "../port_scanner.py")
    )
    result = subprocess.run(
        ["python3", script_path] + args,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    print(f"Running command: python3 {script_path} {' '.join(args)}")
    print(f"STDOUT:\n{result.stdout}")
    print(f"STDERR:\n{result.stderr}")
    return result


# --- Valid Input Tests ---
def test_valid_single_port():
    """Test valid single port input."""
    result = run_cli(["127.0.0.1", "--start", "22", "--end", "22"])
    assert "Port 22:" in result.stdout


def test_valid_range_of_denied_ports():
    """Test valid range of denied ports."""
    result = run_cli(["127.0.0.1", "--start", "1", "--end", "25"])
    assert "Port" in result.stdout  # Check if the output mentions scanned ports


def test_valid_delay_included():
    """Test valid input with delay."""
    result = run_cli(["127.0.0.1", "--start", "22", "--end", "22", "--delay", "100"])
    assert "Port 22:" in result.stdout
