def eliminate_null_and_unit(grammar):
    non_terminals = set()
    for production in grammar:
        non_terminals.add(production[0])

    null_productions = set()
    unit_productions = set()
    new_grammar = set()

    # Find all null and unit productions
    for production in grammar:
        if len(production[1]) == 0:
            null_productions.add(production[0])
        elif len(production[1]) == 1 and production[1][0] in non_terminals:
            unit_productions.add(production)
        else:
            new_grammar.add(production)

    # Remove null and unit productions
    while True:
        removed = False
        for production in new_grammar:
            if production[0] in null_productions:
                new_grammar.remove(production)
                removed = True
                break
            for symbol in production[1]:
                if symbol in null_productions:
                    new_production = (production[0], [x for x in production[1] if x != symbol])
                    if len(new_production[1]) == 0:
                        null_productions.add(new_production[0])
                    else:
                        new_grammar.remove(production)
                        new_grammar.add(new_production)
                        removed = True
                        break
        for unit_production in unit_productions:
            for production in new_grammar:
                if production[0] == unit_production[1][0]:
                    new_production = (unit_production[0], production[1])
                    new_grammar.remove(production)
                    new_grammar.add(new_production)
                    removed = True
                    break
        if not removed:
            break

    return new_grammar


if __name__ == '__main__':
    grammar = set()
    n = int(input('Enter the number of productions: '))
    for i in range(n):
        production = tuple(input('Enter production ' + str(i + 1) + ': ').split())
        grammar.add(production)

    grammar = eliminate_null_and_unit(grammar)
    print('Modified grammar:')
    for production in grammar:
        print(production[0] + ' -> ' + ' '.join(production[1]))
