import graphviz

# Function to create a Graphviz graph from a NFA 5-tuple
def create_nfa_graph(states, alphabet, transitions, start_state, accept_states):
  # Create a new Graphviz graph
  graph = graphviz.Graph(format='png')
  graph.attr(rankdir='LR')

  # Add a node for each state
  for state in states:
    # Use a double circle shape for accept states
    if state in accept_states:
      shape = 'doublecircle'
    else:
      shape = 'circle'
    graph.node(state, shape=shape)

  # Add an edge for each transition
  for transition in transitions:
    from_state, symbol, to_state = transition
    graph.edge(from_state, to_state, label=symbol)

  return graph

# Function to test a string against an NFA
def test_string(states, alphabet, transitions, start_state, accept_states, string):
  # Create a set of current states
  current_states = set()
  current_states.add(start_state)

  # Iterate through each symbol in the string
  for symbol in string:
    # Create a set of next states
    next_states = set()

    # Iterate through each current state
    for current_state in current_states:
      # Iterate through each transition
      for transition in transitions:
        # The transition is a tuple (from_state, symbol, to_state)
        from_state, trans_symbol, to_state = transition
        if current_state == from_state and symbol == trans_symbol:
          # Add the to_state to the set of next states
          next_states.add(to_state)

    # Update the current states to the next states
    current_states = next_states

  # Check if any of the current states are accept states
  for current_state in current_states:
    if current_state in accept_states:
      return True

  return False

# Prompt the user to enter the NFA 5-tuple
states = input("Enter the states (comma-separated): ").split(',')
alphabet = input("Enter the alphabet (comma-separated): ").split(',')
transitions_str = input("Enter the transitions in the form 'from_state,symbol,to_state' (comma-separated): ")
transitions = [tuple(transition.split(',')) for transition in transitions_str.split(',,')]
start_state = input("Enter the start state: ")
accept_states_str = input("Enter the accept states (comma-separated): ")
accept_states = accept_states_str.split(',')

# Create the NFA graph
nfa_graph = create_nfa_graph(states, alphabet, transitions, start_state, accept_states)

# Render the graph and save it to a file
nfa_graph.render('nfa',view=True)

string = input("Enter a string to test: ")
if test_string(states, alphabet, transitions, start_state, accept_states, string):
  print("The string is accepted by the NFA.")
else:
  print("The string is not accepted by the NFA.")