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
    assert "Port" in result.stdout


def test_valid_delay_included():
    """Test valid input with delay."""
    result = run_cli(["127.0.0.1", "--start", "22", "--end", "22", "--delay", "100"])
    assert "Port 22:" in result.stdout


# --- Invalid Input Tests ---
def test_invalid_ip_address():
    """Test invalid IP address."""
    result = run_cli(["999.999.999.999", "--start", "22", "--end", "22"])
    assert "🚫 Invalid IP address" in result.stdout  # Check in stdout


def test_invalid_port_range_negative():
    """Test invalid negative port range."""
    result = run_cli(["127.0.0.1", "--start", "-10", "--end", "50"])
    assert "🚫 Port range must be between 1 and 65535" in result.stdout


def test_invalid_port_range_exceeding_max():
    """Test invalid port range exceeding maximum."""
    result = run_cli(["127.0.0.1", "--start", "1", "--end", "70000"])
    assert "🚫 Port range must be between 1 and 65535" in result.stdout


def test_invalid_port_range_reversed():
    """Test invalid reversed port range."""
    result = run_cli(["127.0.0.1", "--start", "100", "--end", "50"])
    assert "🚫 Start port cannot be greater than end port" in result.stdout


def test_invalid_delay_negative():
    """Test invalid negative delay."""
    result = run_cli(["127.0.0.1", "--start", "22", "--end", "22", "--delay", "-100"])
    assert "🚫 Delay must be a non-negative integer" in result.stdout


# --- Missing or Unexpected Arguments Tests ---
def test_missing_target_ip():
    """Test missing target IP."""
    result = run_cli(["--start", "22", "--end", "22"])
    assert "the following arguments are required: target" in result.stderr


def test_unexpected_additional_argument():
    """Test unexpected additional argument."""
    result = run_cli(["127.0.0.1", "--start", "22", "--end", "22", "--foo", "123"])
    assert "unrecognized arguments: --foo" in result.stderr


def test_no_arguments():
    """Test no arguments provided."""
    result = run_cli([])
    assert "usage: port_scanner.py" in result.stderr


def test_help_command():
    """Test the help command."""
    result = run_cli(["--help"])
    assert "usage: port_scanner.py" in result.stdout


def test_wrong_argument_type_non_integer_ports():
    """Test wrong argument type for ports (non-integer)."""
    result = run_cli(["127.0.0.1", "--start", "abc", "--end", "80"])
    assert "argument --start: invalid int value" in result.stderr


def test_wrong_argument_type_non_integer_delay():
    """Test wrong argument type for delay (non-integer)."""
    result = run_cli(["127.0.0.1", "--start", "22", "--end", "22", "--delay", "xyz"])
    assert "argument --delay: invalid int value" in result.stderr


def test_wrong_argument_type_non_ip_target():
    """Test wrong argument type for target IP (non-IP)."""
    result = run_cli(["abc.def", "--start", "22", "--end", "22"])
    assert "🚫 Invalid IP address" in result.stdout


def test_missing_port_range_parameters():
    """Test missing port range parameters."""
    result = run_cli(["127.0.0.1", "--start", "--end"])
    assert "argument --start: expected one argument" in result.stderr
