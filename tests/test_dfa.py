import sys  # Import the sys module, which provides access to system-specific parameters and functions
import os   # Import the os module, which allows interaction with the operating system (such as file paths)

# Add the src directory to sys.path so we can import dfa.py
# sys.path is a list of directories Python searches for modules when importing.
# By appending a new directory path, we're telling Python where to find additional files.
sys.path.append(os.path.abspath('/home/linux_subsystem/WSL_Coding_Space/CS361/p1_overview/src/p1_overview'))

# Import the DFA class and parse_dfa_file function
# The DFA class will handle the DFA logic, and the parse_dfa_file function will handle reading the input file and parsing it into useful components.
from dfa import DFA, parse_dfa_file

# Define the path to the input file
# This variable stores the location of the input file containing the DFA's description and test strings.
file_path = "/home/linux_subsystem/WSL_Coding_Space/CS361/p1_overview/data/input/p1tc1.txt"

# Parse the DFA and the test strings from the input file
# The parse_dfa_file function is called with the file_path as an argument.
# It returns two values: `dfa`, which is an object of the DFA class, and `test_strings`, which is a list of strings to test against the DFA.
dfa, test_strings = parse_dfa_file(file_path)

# Ensure dfa is the DFA object and test_strings is the list of test strings
# isinstance() is used to check if 'dfa' is an instance of the DFA class.
if isinstance(dfa, DFA):
    # Loop through each string in the test_strings list
    # For each string, we call the 'run' method of the dfa object to check if the DFA accepts or rejects the string.
    for string in test_strings:
        result = dfa.run(string)  # 'run' returns True if the DFA accepts the string, False if it rejects it.
        # Print whether the string is accepted or rejected.
        # The string is accepted if `result` is True, and rejected if `result` is False.
        print(f"The string '{string}' is {'accepted' if result else 'rejected'} by the DFA.")
else:
    # If `dfa` is not an instance of the DFA class, an error message is printed.
    # This handles any unexpected result from the parse_dfa_file function.
    print("Error: Expected a DFA object but received something else.")
