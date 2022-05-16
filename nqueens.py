def is_valid_state(state, n):
    return len(state) == n

def get_candidates(state, n):
    if not state:
        return range(n)
    position =  len(state)
    candidates = set(range(n))

    for row, col in enumerate(state):
        candidates.discard(col)
        distance = position - row
        candidates.discard(col+distance)
        candidates.discard(col-distance)
    return candidates

def state_to_string(state, n):
    result = []
    for i in state:
        string ='.' * i + 'Q' + '.'* (n-i-1)
        result.append(string)
    return result

def search(state, solutions, n):
    if is_valid_state(state, n):
        ste_string = state_to_string(state, n)
        solutions.append(ste_string)
        return
    for candidate in get_candidates(state, n):
        state.append(candidate)
        search(state, solutions, n)
        state.pop()

def solve(n):
    solutions = []
    state = []
    search(state, solutions, n)
    return solutions
print(solve(4))
        
