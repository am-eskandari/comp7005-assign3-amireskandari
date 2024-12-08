from tabulate import tabulate

# Define states and descriptions
states = [
    {
        "State": "START",
        "Description": "Port scanner initializes and validates user input.",
    },
    {"State": "SCAN_PORT", "Description": "Sends a SYN packet to a target port."},
    {"State": "WAIT_RESPONSE", "Description": "Waits for a response from the target."},
    {"State": "PROCESS_RESULT", "Description": "Processes the result of the scan."},
    {"State": "TERMINATE", "Description": "Completes the scan and logs results."},
]

# Define transitions
transitions = [
    {"From State": "START", "To State": "SCAN_PORT", "Function": "validate_inputs"},
    {
        "From State": "SCAN_PORT",
        "To State": "WAIT_RESPONSE",
        "Function": "send_syn_packet",
    },
    {
        "From State": "WAIT_RESPONSE",
        "To State": "PROCESS_RESULT",
        "Function": "receive_response",
    },
    {
        "From State": "PROCESS_RESULT",
        "To State": "SCAN_PORT",
        "Function": "log_results (for next port)",
    },
    {
        "From State": "PROCESS_RESULT",
        "To State": "TERMINATE",
        "Function": "log_results (on scan completion)",
    },
]


# Generate tables
def generate_fsm_tables():
    print("FSM States:")
    print(tabulate(states, headers="keys", tablefmt="grid"))
    print("\nFSM State Transitions:")
    print(tabulate(transitions, headers="keys", tablefmt="grid"))


if __name__ == "__main__":
    generate_fsm_tables()
