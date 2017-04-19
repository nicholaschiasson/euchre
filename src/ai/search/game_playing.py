def alphabeta(state, heuristics, depth=float("inf")):
    return maxvalue(state, heuristics, float("-inf"), float("inf"), depth)

def maxvalue(state, heuristics, a, b, depth):
    adjacent_states = state.get_adjacent_states()
    if depth < 1 or len(adjacent_states) < 1:
        heuristic_avg = 0.0
        for f in heuristics:
            heuristic_avg += f(state)
        return heuristic_avg
    for s in adjacent_states:
        a = max(a, minvalue(s, heuristics, a, b, depth - 1))
        if a >= b:
            return a
    return a

def minvalue(state, heuristics, a, b, depth):
    adjacent_states = state.get_adjacent_states()
    if depth < 1 or len(adjacent_states) < 1:
        heuristic_avg = 0.0
        for f in heuristics:
            heuristic_avg += f(state)
        return heuristic_avg
    for s in adjacent_states:
        b = min(b, maxvalue(s, heuristics, a, b, depth - 1))
        if b <= a:
            return b
    return b
