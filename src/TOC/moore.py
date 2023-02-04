import graphviz

def draw_moore_machine(states, alphabet, start_state, output_function):
    graph = graphviz.Digraph(format='png')
    graph.attr(rankdir='LR', size='8,5')
    for state in states:
        label = state + '\n' + output_function[state]
        graph.node(state, label=label)
    for state in transition_function:
        for char in transition_function[state]:
            graph.edge(state, transition_function[state][char], label=char)
    return graph

if __name__ == '__main__':
    states = input("Enter states separated by comma: ").split(',')
    alphabet = input("Enter alphabet characters separated by comma: ").split(',')
    transition_function = {}
    for state in states:
        transition_function[state] = {}
        for char in alphabet:
            transition_function[state][char] = input(f"Enter next state for state {state} on {char}: ")
    start_state = input("Enter start state: ")
    output_function = {}
    for state in states:
        output_function[state] = input(f"Enter output function for state {state}: ")
    machine = draw_moore_machine(states, alphabet, start_state, output_function)
    machine.render("moore_machine")

    input_string = input("Enter input string: ")
    state = start_state
    output_string = ""
    for char in input_string:
        state = transition_function[state][char]
        output_string += output_function[state]
    output_string += output_function[state]
    print("Output string:", output_string)