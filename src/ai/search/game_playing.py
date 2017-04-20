def alphabeta(state, heuristic, depth=float("inf")):
    return maxvalue(state, heuristic, float("-inf"), float("inf"), depth)

def maxvalue(state, heuristic, a, b, depth):
    adjacent_states = state.get_adjacent_states()
    if depth < 1 or len(adjacent_states) < 1:
        return heuristic(state)
    for s in adjacent_states:
        a = max(a, minvalue(s, heuristic, a, b, depth - 1))
        if a >= b:
            break
    return a

def minvalue(state, heuristic, a, b, depth):
    adjacent_states = state.get_adjacent_states()
    if depth < 1 or len(adjacent_states) < 1:
        return heuristic(state)
    for s in adjacent_states:
        b = min(b, maxvalue(s, heuristic, a, b, depth - 1))
        if b <= a:
            break
    return b
