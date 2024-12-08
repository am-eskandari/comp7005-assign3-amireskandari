from datetime import datetime

from graphviz import Digraph

# Define states based on the scanner code
states = [
    {"State": "START", "Description": "Initializes the scanner and validates input."},
    {
        "State": "SCAN_PORT",
        "Description": "Sends a SYN packet to a specified target port.",
    },
    {
        "State": "WAIT_RESPONSE",
        "Description": "Waits for a response from the target port.",
    },
    {
        "State": "PROCESS_RESULT",
        "Description": "Processes the response to determine port status.",
    },
    {
        "State": "LOG_RESULT",
        "Description": "Logs the result and prepares for the next port.",
    },
    {"State": "TERMINATE", "Description": "Completes the scan and exits gracefully."},
]

# Define transitions based on the scanner code
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
        "To State": "LOG_RESULT",
        "Function": "determine_port_status",
    },
    {"From State": "LOG_RESULT", "To State": "SCAN_PORT", "Function": "next_port"},
    {
        "From State": "LOG_RESULT",
        "To State": "TERMINATE",
        "Function": "all_ports_scanned",
    },
    {"From State": "START", "To State": "TERMINATE", "Function": "invalid_input"},
    {
        "From State": "WAIT_RESPONSE",
        "To State": "TERMINATE",
        "Function": "handle_interrupt",
    },
]


# Create FSM diagram
def generate_fsm_diagram(output_file="fsm_diagram"):
    # Add timestamp to avoid overwriting files
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file_with_timestamp = f"{output_file}_{timestamp}"

    fsm = Digraph("FSM", format="png")
    fsm.attr(rankdir="TB", size="10,15", dpi="1200")  # Adjust size and resolution

    # Add states with color coding
    for state in states:
        fill_color = (
            "lightgreen"
            if state["State"] == "START"
            else "lightcoral" if state["State"] == "TERMINATE" else "lightblue"
        )
        fsm.node(
            state["State"],
            label=f"{state['State']}\n{state['Description']}",
            shape="ellipse",
            style="filled",
            fillcolor=fill_color,
        )

    # Add transitions
    for transition in transitions:
        fsm.edge(
            transition["From State"],
            transition["To State"],
            label=transition["Function"],
        )

    # Render the FSM diagram
    fsm.render(output_file_with_timestamp, cleanup=True)
    return output_file_with_timestamp + ".png"


# Generate the diagram
output_path = generate_fsm_diagram()
print(f"FSM diagram saved to {output_path}")
