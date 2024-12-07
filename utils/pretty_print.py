import sys


def display_error(message):
    """Display error messages in a pretty format."""
    print("\n❌ Error:")
    print(f"   {message}\n", file=sys.stdout)


def display_results(results):
    """Display the port scanning results."""
    print("\n📋 Scan Results:")
    for port, status in results:
        emoji = "🟢" if status == "Open" else "🔴" if status == "Closed" else "🟡"
        print(f"   {emoji} Port {port}: {status}")
    print("\n✅ Scan completed successfully.\n")


def display_info(message):
    """Display informational messages."""
    print(f"\nℹ️ {message}\n")
