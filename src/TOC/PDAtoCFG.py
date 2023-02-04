from collections import defaultdict
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
    def to_cfg(self):
        # Create a dictionary to store the rules
        rules = defaultdict(list)

        # Create a starting rule
        starting_rule = self.initial_state + self.initial_stack_symbol
        rules[starting_rule].append('#')

        # Loop through all the transitions
        for transition in self.transitions:
            current_state, input_symbol, stack_symbol, next_state, next_stack_symbol = transition
            current_rule = current_state + stack_symbol
            next_rule = next_state + next_stack_symbol

            rules[current_rule].append(input_symbol + next_rule)
        # Return the rules
        return rules

if __name__ == '__main__':
    pda = PDA(['q0', 'q1', 'q2'],
              ['0', '1'],
              ['$', '0', '1'],
              [('q0', '0', '$', 'q1', '0'),
               ('q1', '0', '0', 'q1', '0'),
               ('q1', '1', '0', 'q2', '$'),
               ('q2', '1', '1', 'q2', '1')],
              'q0', '$',
              ['q2'])
    cfg_rules = pda.to_cfg()
    print(cfg_rules)