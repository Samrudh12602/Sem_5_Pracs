def validate_dfa(states, alphabet, transition_function, start_state, accept_states, string):
    current_state = start_state
    for char in string:
        if char not in alphabet:
            return False
        current_state = transition_function[current_state][alphabet.index(char)]
    return current_state in accept_states

if __name__ == '__main__':
    states = input("Enter states separated by comma: ").split(',')
    alphabet = input("Enter alphabet characters separated by comma: ").split(',')
    transition_function = {}
    for state in states:
        transition_function[state] = {}
        for char in alphabet:
            transition_function[state][alphabet.index(char)] = input(f"Enter transition for state {state} on {char}: ")
    start_state = input("Enter start state: ")
    accept_states = input("Enter accept states separated by comma: ").split(',')
    string = input("Enter a string to validate: ")
    while string != 'stop':
        if validate_dfa(states, alphabet, transition_function, start_state, accept_states, string):
            print("Accepted")
        else:
            print("Rejected")
        string = input("Enter a string to validate: ")