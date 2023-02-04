import graphviz as gv

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

    dot = gv.Digraph(format='png')
    dot.attr(rankdir='LR', size='8,5')
    for state in states:
        if state in accept_states:
            dot.attr('node', shape='doublecircle')
        else:
            dot.attr('node', shape='circle')
        dot.node(state)
    for state in states:
        for char in alphabet:
            next_state = transition_function[state][alphabet.index(char)]
            dot.edge(state, next_state, label=char)
    dot.render('dfa')

    string = input("Enter a string to validate: ")
    while string != 'stop':
        if validate_dfa(states, alphabet, transition_function, start_state, accept_states, string):
            print("Accepted")
        else:
            print("Rejected")
        string = input("Enter a string to validate: ")