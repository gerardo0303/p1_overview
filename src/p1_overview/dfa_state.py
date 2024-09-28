class State_of_DFA:
    def __init__(self, name_of_state, is_accepting_state=False):
        """
        Initializes a new state in the DFA.
        
        Parameters:
        name_of_state (str): The name of the state (e.g., "q0", "q1").
        is_accepting_state (bool): Whether this state is an accepting state.
        
        Attributes:
        name_of_state (str type): Stores the name of the state.
        is_accepting_state (bool type): Indicates if the state is an accepting state.
        transitions_dict (dictionary type): A dictionary mapping input symbols to next states.
        """
        # Store the name of the state.
        self.name_of_state = name_of_state

        # Specify whether this state is an accepting state. (bool type)
        # True means it's an accepting state False means it's not we start with it false.
        self.is_accepting_state = is_accepting_state

        # Initialize an empty dictionary to store transitions.
        self.transitions_dictionary = {}

    def add_transition(self, input_symbol, next_state):
        """
        Adds a transition from this state to another state based on an input symbol.
        
        Parameters:
        input_symbol (of str type): The input symbol that desiceds the transition.
        next_state 'State_of_DFA': The state to transition to.
        
        What this does:
        It updates the transitions_dict dictionary so that when the DFA reads `input_symbol`,
        it knows which state to move to next.
        """
        # Add the transition based on the input symbol to the next state.
        self.transitions_dictionary[input_symbol] = next_state

    def get_next_state(self, input_symbol):
        """
        Retrieves the next state based on the input symbol.
        
        Parameters:
        input_symbol (str): The input symbol to check against this state's transitions.
        
        Returns:
        State_of_DFA: The state to transition to, or None if the symbol isn't found.
        
        Why it's important:
        This method allows the DFA to decide where to move next when it reads a symbol.
        """
        # Return the next state for the given symbol, or None if the symbol isn't found.
        return self.transitions_dictionary.get(input_symbol)

    def __str__(self):
        """
        Provides a string representation of the state, useful for debugging.
        
        Returns:
        str: A string showing the state's name and whether it's accepting.
        
        Example:
        State(q0, Non-accepting)
        """
        # Check if the state is accepting or non-accepting.
        state_type = "Accepting" if self.is_accepting_state else "Non-accepting"

        # Return a string representing the state's name and its type.
        return f"State({self.name_of_state}, {state_type})"