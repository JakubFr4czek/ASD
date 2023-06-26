def prom(i, A, L1, L2):

    if L1 > 0 and L2 > 0:
        return max(prom(i + 1, A, L1 - A[i], L2), prom(i + 1, A, L1, L2 - A[i]))
    if L1 <= 0 and L2 > 0:
        return prom(i, A, L1, L2 - A[i - 1])
    elif L2 <= 0 and L1 > 0:
        return prom(i, A, L1 - A[i - 1], L2)
    else:
        return i - 1


A = [5,4,2,1,6,7,4,2]

L1 = 10
L2 = 9

print(prom(0, A, L1, L2))