def moore(states, alphabet, start_state, next_state, output_function, input_string):
    state = start_state
    output = ""
    for char in input_string:
        output += output_function[state]
        state = next_state[state][char]
    output += output_function[state]
    return output

if __name__ == "__main__":
    states = input("Enter states separated by comma: ").split(',')
    alphabet = input("Enter alphabet characters separated by comma: ").split(',')
    start_state = input("Enter start state: ")
    next_state = {}
    output_function = {}
    for state in states:
        next_state[state] = {}
        for char in alphabet:
            next_state[state][char] = input("Enter next state for state {} on {}: ".format(state, char))
        output_function[state] = input("Enter output function for state {}: ".format(state))
    input_string = input("Enter input string: ")
    output = moore(states, alphabet, start_state, next_state, output_function, input_string)
    print("Output string:", output)