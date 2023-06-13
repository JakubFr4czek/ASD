#O(n^2)

def tsm(i, j, F, D):

    if F[i][j] != float('inf'): return F[i][j]

    if i == j - 1:
        best = float('inf')

        for k in range(j - 1):
            best = min(best, tsm(k, j - 1, F, D) + D[k][j])
        F[j - 1][j] = best
    else:
        F[i][j] = tsm(i, j - 1, F, D) + D[j - 1][j] #Jak są obok
    
    return F[i][j]


D = [

    [0, 10, 15, 20],
    [5, 0, 9, 10],
    [6, 13, 0, 12],
    [8, 8, 9, 0]

]


F = [ [ float('inf') for j in range(len(D)) ] for i in range(len(D))]
F[0][1] = D[0][1]




print(tsm(0, 3, F, D))