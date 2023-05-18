from collections import deque


def FordFulkerson(M, s, t):
    


        

G1 = [ #5

    [(1,3), (3,3)],
    [(2,4)],
    [(3,1), (4,2)],
    [(4,2), (5,6)],
    [(6,1)],
    [(6,9)],
    []

]

M = [ [0 for j in range(len(G))] for i in range(len(G))]

for i in range(len(G)):
    for j in range(len(G[i])):
        M[i][G[i][j][0]] = G[i][j][1]
        M[G[i][j][0]][i] = 0

print(FordFulkerson(M, 0, len(G) - 1))