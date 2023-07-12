DP = dict()

def frog(i, energy, C):
    global DP
    # print(i, energy, energy + i, len(C))
    if energy + i >= len(C):
        return 1
    if i >= len(C):
        return float("inf")
    key = (i, energy) 
    if key in DP:
        return DP[key]
    jumps = [frog(i + x, energy - x + C[i + x], C) for x in range(1, min(energy - i, len(C) - i - 1))]
    if len(jumps) == 0:
        jumps = [float("inf")]
    lowest_jumps = min(jumps)
    DP[key] = lowest_jumps + 1
    return lowest_jumps + 1

lilypads = [2, 0, 0]

print(frog(0, lilypads[0], lilypads))
