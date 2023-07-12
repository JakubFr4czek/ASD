
def suma(T, i, j):

    res = 0

    for x in range(i, j + 1):
        res += T[x]

    return res

def f(T, i, j):

    if i > j: return float('-inf')

    return max(abs(suma(T, i, j)), min(f(T, i + 1, j), f(T, i, j - 1)))


T = [1, -5, 2]

print(f(T, 0, 2))
