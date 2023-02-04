import graphviz

class TuringMachine:
    def __init__(self, states, alphabet, transitions, initial_state, final_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.initial_state = initial_state
        self.final_states = final_states

    def accept(self, string):
        state = self.initial_state
        tape = list(string) + ['']
        index = 0
        while state not in self.final_states:
            found_transition = False
            for transition in self.transitions:
                if transition[0] == state and transition[1] == tape[index]:
                    state = transition[2]
                    tape[index] = transition[3]
                    if transition[4] == 'R':
                        index += 1
                    elif transition[4] == 'L':
                        index -= 1
                    found_transition = True
                    break
            if not found_transition:
                return False
        return True

    def draw(self):
        dot = graphviz.Digraph(format='png')
        dot.attr(rankdir='LR', size='8,5')
        for state in self.states:
            if state == self.final_states:
                dot.node(state, state, shape='doublecircle')
            elif state in self.initial_state:
                dot.node(state, state, shape='circle')
            else:
                dot.node(state, state)
        for transition in self.transitions:
            dot.edge(transition[0], transition[2],label='{} / {} , {} / {}'.format(transition[1], transition[3], transition[4]))
        return dot

if __name__ == '__main__':
    states = input("Enter the states (comma-separated): ").strip().split(',')
    alphabet = input("Enter the alphabet (comma-separated): ").strip().split(',')
    transitions = []
    print("Enter the transitions (q0, 0, q1, 0, R): ")
    while True:
        transition = input().strip().split(',')
        if len(transition) == 1 and transition[0] == '':
            break
        transitions.append(transition)
    initial_state = input("Enter the initial state: ").strip()
    final_states = input("Enter the final states (comma-separated): ").strip().split(',')

    tm = TuringMachine(states, alphabet, transitions, initial_state, final_states)
    while True:
        string = input('Enter a string to test or type "stop": ')
        if string == 'stop':
            break
        result = 'accepted' if tm.accept(string) else 'rejected'
        print('The string is {} by the Turing machine.'.format(result))
    tm.draw().render('tm')