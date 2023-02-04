def transition(state, char):
    if state == 0:
        if char == '0':
            return (1, '0', 'R')
        elif char == '1':
            return (2, '1', 'R')
        elif char == 'B':
            return (0, 'B', 'R')
    elif state == 1:
        if char == '0':
            return (1, '0', 'R')
        elif char == '1':
            return (1, '1', 'R')
        elif char == 'B':
            return (3, 'B', 'L')
    elif state == 2:
        if char == '0':
            return (2, '0', 'R')
        elif char == '1':
            return (2, '1', 'R')
        elif char == 'B':
            return (4, 'B', 'L')
    elif state == 3:
        if char == '0':
            return (3, '0', 'L')
        elif char == '1':
            return (3, '1', 'L')
        elif char == 'B':
            return (5, '0', 'R')
    elif state == 4:
        if char == '0':
            return (4, '0', 'L')
        elif char == '1':
            return (4, '1', 'L')
        elif char == 'B':
            return (5, '1', 'R')
    elif state == 5:
        if char == '0':
            return (5, '0', 'R')
        elif char == '1':
            return (5, '1', 'R')
        elif char == 'B':
            return (0, 'B', 'R')
    return (None, None, None)

def copy_string(input_string):
    tape = ['B'] + list(input_string) + ['B']
    index = 1
    state = 0
    while state is not None:
        state, tape[index], direction = transition(state, tape[index])
        if direction == 'R':
            if index == len(tape) - 1:
                tape.append('B')
            index += 1
        elif direction == 'L':
            if index == 0:
                tape.insert(0, 'B')
                index += 1
            index -= 1
    return ''.join(tape[1:-1])

input_string = '01'
print("Copied string: ", copy_string(input_string))
