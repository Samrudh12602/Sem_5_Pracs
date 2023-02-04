import graphviz


class PDA:
    def __init__(self, states, alphabet, stack_alphabet, transitions, initial_state, initial_stack_symbol,
                 final_states):
        self.states = states
        self.alphabet = alphabet
        self.stack_alphabet = stack_alphabet
        self.transitions = transitions
        self.initial_state = initial_state
        self.initial_stack_symbol = initial_stack_symbol
        self.final_states = final_states

    def accept(self, string):
        stack = [self.initial_stack_symbol]
        state = self.initial_state
        for char in string:
            found_transition = False
            for transition in self.transitions:
                if transition[0] == state and transition[1] == char and transition[2] == stack[-1]:
                    state = transition[3]
                    stack.pop()
                    if transition[4] != '':
                        stack.append(transition[4])
                    found_transition = True
                    break
            if not found_transition:
                return False
        return state in self.final_states

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
            dot.edge(transition[0], transition[3],
                     label='{} / {} -> {}'.format(transition[1], transition[2], transition[4]))
        return dot


if __name__ == '__main__':
    pda = PDA(['q0', 'q1', 'q2'],
              ['0', '1'],
              ['$', '0', '1'],
              [('q0', '0', '$', 'q1', '0'),
               ('q1', '0', '0', 'q1', '0'),
               ('q1', '1', '0', 'q2', '$'),],
              'q0', '$','q2')
    while True:
        string = input('Enter a string to test or type "stop": ')
        if string == 'stop':
            break
        result = 'accepted' if pda.accept(string) else 'rejected'
        print('The string is {} by the PDA.'.format(result))
    pda.draw().render('pda')
