from dfa_state import State_of_DFA  # Import the 'State_of_DFA' class from the 'dfa_state' file.

class DFA:
    def __init__(self):
        # Constructor method that initializes the DFA object when created.
        # 'self.states' is a dictionary to store states in the DFA, with state names as keys and state objects as values.
        self.states = {}
        # 'self.start_state' will store the starting state of the DFA.
        self.start_state = None
        # 'self.accepting_states' is a set that will contain all the accepting states.
        self.accepting_states = set()

    def add_state(self, state_name, is_accepting=False):
        # This method adds a new state to the DFA.
        # 'state_name' is the name of the state to be added.
        # 'is_accepting' is a boolean value indicating if the state is an accepting state (True if it is).
        
        # Create a new instance of 'State_of_DFA' with the given 'state_name' and 'is_accepting' status.
        state = State_of_DFA(state_name, is_accepting)
        
        # Add the newly created state to the 'states' dictionary, using 'state_name' as the key.
        self.states[state_name] = state
        
        # If the state is an accepting state, add it to the 'accepting_states' set.
        if is_accepting:
            self.accepting_states.add(state)

    def set_start_state(self, state_name):
        # This method sets the start state of the DFA.
        # 'state_name' is the name of the start state.
        
        # Retrieve the state object corresponding to 'state_name' from the 'states' dictionary and set it as the start state.
        self.start_state = self.states.get(state_name)

    def add_transition(self, from_state, symbol, to_state):
        # This method adds a transition between states in the DFA.
        # 'from_state' is the name of the state where the transition starts.
        # 'symbol' is the input symbol that causes the transition.
        # 'to_state' is the name of the state where the transition leads.

        # Retrieve the state object for the 'from_state' from the 'states' dictionary.
        from_state_obj = self.states.get(from_state)
        # Retrieve the state object for the 'to_state' from the 'states' dictionary.
        to_state_obj = self.states.get(to_state)
        
        # Check if both 'from_state_obj' and 'to_state_obj' exist (i.e., the states are valid).
        if from_state_obj and to_state_obj:
            # If both states are valid, call the 'add_transition' method of 'from_state_obj' to add a transition.
            from_state_obj.add_transition(symbol, to_state_obj)
    
    def run(self, input_string):
        # This method simulates the DFA running on an input string.
        # 'input_string' is the string to be processed by the DFA.
        
        # Start processing from the 'start_state'.
        current_state = self.start_state
        
        # Print the starting state for debugging purposes.
        print(f"Starting at state: {current_state}\n")
        
        # Loop over each symbol in the input string.
        for symbol in input_string:
            # Print the current state and the symbol being read for debugging.
            print(f"At state: {current_state}, reading symbol: {symbol}")
            
            # Use the 'get_next_state' method to find the next state based on the current symbol.
            current_state = current_state.get_next_state(symbol)
            
            # If there is no valid transition for the current symbol (i.e., DFA reaches an undefined state).
            if current_state is None:
                # Print an error message and reject the string (return False).
                print(f"No transition found for symbol {symbol}. Rejecting string.")
                return False
        
        # After processing the entire input string, print the final state for debugging.
        print(f"Ended at state: {current_state}")
        
        # Check if the final state is an accepting state, and return True if it is, or False otherwise.
        return current_state.is_accepting_state

def parse_dfa_file(file_path):
    # This function reads a DFA definition from a file and creates a DFA object.
    # 'file_path' is the path to the file containing the DFA definition.

    # Open the file in read mode and process each line.
    with open(file_path, 'r') as file:
        # Strip empty lines and whitespace from each line.
        lines = [line.strip() for line in file if line.strip()]
    
    # Debugging output to check the lines that were read.
    print(f"DEBUG: Lines after stripping empty lines:\n{lines}")

    # First line of the file contains the accepting states.
    accepting_states = lines[0].split()
    
    # Debugging output to check the accepting states.
    print(f"DEBUG: Accepting states: {accepting_states}")

    # Second line contains the start state.
    start_state = lines[1].strip()
    
    # Debugging output to check the start state.
    print(f"DEBUG: Start state: {start_state}")

    # Check if the third line contains other states or transitions.
    other_states = []
    
    # If the third line is a transition (e.g., "s0s1s2" format), process transitions directly.
    if len(lines[2].split()[0]) == 3:
        transitions = lines[2].split()
        test_strings = lines[3:]  # Everything after transitions are test strings.
    else:
        # If it's not a transition, the third line contains other states.
        other_states = lines[2].split()
        transitions = lines[3].split()
        test_strings = lines[4:]

    # Debugging outputs to check other states, transitions, and test strings.
    print(f"DEBUG: Other states: {other_states}")
    print(f"DEBUG: Transitions: {transitions}")
    print(f"DEBUG: Test strings: {test_strings}")

    # Create a DFA object.
    dfa = DFA()

    # Add start state, accepting states, and other states to the DFA.
    all_states = set([start_state] + accepting_states + other_states)
    for state in all_states:
        # Determine if the state is an accepting state.
        is_accepting = state in accepting_states
        # Add the state to the DFA.
        dfa.add_state(state, is_accepting)

    # Process transitions from the file.
    for transition in transitions:
        # Ensure that the transition is properly formatted (should be 3 characters: from_state, symbol, to_state).
        if len(transition) != 3:
            # Print a warning if the transition is malformed.
            print(f"Warning: Malformed transition '{transition}' in input file.")
            continue
        
        # Extract the from_state, symbol, and to_state from the transition string.
        from_state = transition[0]
        input_symbol = transition[1]
        to_state = transition[2]
        
        # Add the transition to the DFA.
        dfa.add_transition(from_state, input_symbol, to_state)
        
        # Debugging output to check the added transition.
        print(f"Added transition: {from_state} --{input_symbol}--> {to_state}")

    # Set the start state for the DFA.
    dfa.set_start_state(start_state)
    
    # Return the DFA object and the test strings.
    return dfa, test_strings
