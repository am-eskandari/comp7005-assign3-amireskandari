import socket


def validate_ip(target):
    """Validate the target IP address."""
    try:
        socket.inet_aton(target)
    except socket.error:
        raise ValueError("🚫 Invalid IP address.")


def validate_port_range(start_port, end_port):
    """Validate the port range."""
    if not (1 <= start_port <= 65535 and 1 <= end_port <= 65535):
        raise ValueError("🚫 Port range must be between 1 and 65535.")
    if start_port > end_port:
        raise ValueError("🚫 Start port cannot be greater than end port.")


def validate_delay(delay):
    """Validate the delay."""
    if delay < 0:
        raise ValueError("🚫 Delay must be a non-negative integer.")
