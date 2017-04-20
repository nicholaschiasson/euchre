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

def paranoid_alphabeta(state, heuristic, depth=float("inf"), enemies=4):
    return paranoid_maxvalue(state, heuristic, float("-inf"), float("inf"), depth, enemies)

def paranoid_maxvalue(state, heuristic, a, b, depth, enemies):
    adjacent_states = state.get_adjacent_states()
    if depth < 1 or len(adjacent_states) < 1:
        return heuristic(state)
    for s in adjacent_states:
        a = max(a, paranoid_minvalue(s, heuristic, a, b, depth - 1, enemies, enemies))
        if a >= b:
            break
    return a

def paranoid_minvalue(state, heuristic, a, b, depth, enemies, current_enemy):
    adjacent_states = state.get_adjacent_states()
    if depth < 1 or len(adjacent_states) < 1:
        return heuristic(state)
    for s in adjacent_states:
        if current_enemy > 0:
            b = min(b, paranoid_maxvalue(s, heuristic, a, b, depth - 1, enemies))
        else:
            a = max(a, paranoid_minvalue(s, heuristic, a, b, depth - 1, enemies, enemies - 1))
        if b <= a:
            return b
    return b
