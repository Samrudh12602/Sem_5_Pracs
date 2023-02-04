import graphviz

def draw_mealy(states, alphabet, transition_function, output_function):
    graph = graphviz.Digraph(format="png")
    graph.attr(rankdir='LR', size='8,5')
    for state in states:
            graph.node(state)
    for char in alphabet:
        for state in states:
            if transition_function[char][state] != '':
                graph.edge(state, transition_function[char][state], label=char + '/' + output_function[char][state])
    return graph

def test_mealy(states, alphabet, transition_function, output_function, start_state, test_string):
    state = start_state
    output = ''
    for char in test_string:
        output += output_function[char][state]
        state = transition_function[char][state]
    return output

if __name__ == '__main__':
    test_string=''
    states = input("Enter states separated by comma: ").split(',')
    alphabet = input("Enter alphabet characters separated by comma: ").split(',')
    transition_function = {}
    output_function = {}
    for char in alphabet:
        transition_function[char] = {}
        output_function[char] = {}
        for state in states:
            transition_function[char][state] = input(f"Enter transition for state {state} on {char}: ").split(',')[0]
            output_function[char][state] = input(f"Enter output for state {state} on {char}: ").split(',')[0]
    start_state = input("Enter start state: ")
    while test_string!='stop':
        test_string = input("Enter test string: ")
        output = test_mealy(states, alphabet, transition_function, output_function, start_state, test_string)
        print("Output:", output)

    graph = draw_mealy(states, alphabet, transition_function, output_function)
    graph.render("mealy")