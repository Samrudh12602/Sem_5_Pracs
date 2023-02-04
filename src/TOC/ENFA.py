import graphviz

def epsilon_closure(state, epsilon_transitions):
    closure = {state}
    stack = [state]
    while stack:
        state = stack.pop()
        for next_state in epsilon_transitions[state]:
            if next_state not in closure:
                closure.add(next_state)
                stack.append(next_state)
    return closure

def draw_enfa(states, alphabet, transition_function, start_state, accept_states):
    graph = graphviz.Digraph(format="png")
    graph.attr(rankdir='LR', size='8,5')
    for state in states:
        if state == start_state:
            graph.node(state, shape='circle')
        elif state in accept_states:
            graph.node(state, shape='doublecircle')
        else:
            graph.node(state)
    for from_state in transition_function[""]:
        for to_state in transition_function[""][from_state]:
            if to_state:
                graph.edge(from_state, to_state, label='ε', fontcolor='blue')
    for char in alphabet:
        for from_state in transition_function[char]:
            for to_state in transition_function[char][from_state]:
                if to_state:
                    graph.edge(from_state, to_state, label=char)
    return graph

def test_string(states, alphabet, transition_function, start_state, accept_states, string):
    current_states = epsilon_closure(start_state, transition_function[""])
    for char in string:
        next_states = set()
        for state in current_states:
            next_states |= set(transition_function[char].get(state, []))
        current_states = set().union(*[epsilon_closure(state, transition_function[""]) for state in next_states])
    return bool(current_states & set(accept_states))

if __name__ == '__main__':
    states = input("Enter states separated by comma: ").split(',')
    alphabet = input("Enter alphabet characters separated by comma: ").split(',')
    transition_function = {}
    for char in ['', *alphabet]:
        transition_function[char] = {}
        for state in states:
            transition_function[char][state] = input(f"Enter transition for state {state} on {char}: ").split(',')
    start_state = input("Enter start state: ")
    accept_states = input("Enter accept states separated by comma: ").split(',')

    graph = draw_enfa(states, alphabet, transition_function, start_state, accept_states)
    graph.render("enfa")
    while True:
        string = input("Enter string to test (or stop): ")
        if string.lower() == 'stop':
            break
        if test_string(string, states, alphabet, transition_function, start_state, accept_states):
            print(f"{string} is accepted.")
        else:
            print(f"{string} is not accepted.")