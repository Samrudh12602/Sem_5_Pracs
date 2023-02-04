class TuringMachine:
    def __init__(self, states, alphabet, transitions, initial_state, blank_symbol, final_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.initial_state = initial_state
        self.blank_symbol = blank_symbol
        self.final_states = final_states

    def run(self, string):
        tape = list(string) + [self.blank_symbol]
        state = self.initial_state
        cursor = 0
        while state not in self.final_states:
            current_symbol = tape[cursor]
            transition = self.transitions.get((state, current_symbol))
            if not transition:
                return False
            state, symbol, direction = transition
            tape[cursor] = symbol
            if direction == 'R':
                cursor += 1
            else:
                cursor -= 1
        return True

if __name__ == '__main__':
    states = ['q0', 'q1', 'q2']
    alphabet = ['0', '1']
    transitions = {
        ('q0', '0'): ('q1', '1', 'R'),
        ('q0', '1'): ('q0', '0', 'L'),
        ('q1', '0'): ('q2', '1', 'R'),
        ('q1', '1'): ('q1', '1', 'R'),
        ('q2', '0'): ('q2', '0', 'R'),
        ('q2', '1'): ('q0', '1', 'L'),
    }
    initial_state = 'q0'
    blank_symbol = '_'
    final_states = ['q2']

    tm = TuringMachine(states, alphabet, transitions, initial_state, blank_symbol, final_states)
    while True:
        string = input('Enter a string to test or type "stop": ')
        if string == 'stop':
            break
        result = 'accepted' if tm.run(string) else 'rejected'
        print('The string is {} by the Turing machine.'.format(result))
