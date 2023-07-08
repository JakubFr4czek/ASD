from egzP3btesty import runtests 
from collections import deque

def findSet(parent, x):
    #Bo korzen sie zapetla do samego siebie
    if parent[x] != x:
        #kompresja sciezki
        parent[x] = findSet(parent, parent[x])
    return parent[x]

def Union(parent, rank, x, y):

    x = findSet(parent, x)
    y = findSet(parent, y)

    if rank[x] > rank[y]:
        parent[y] = x
    else:
        parent[x] = y

        if rank[x] == rank[y]:
            rank[y] += 1

def Kruskal(G):

    G.sort(key= lambda temp: temp[2])

    A = deque()

    parent = [i for i in range(len(G))]
    rank = [0 for _ in range(len(G))]

    for i in range(len(G)):
        
        e1, e2, weight = G[i]

        k1 = findSet(parent, e1)
        k2 = findSet(parent, e2)

        if k1 != k2:
            A.append( G[i] )
            Union(parent, rank, e1, e2)
    
    return A

def lufthansa ( G ):

    G2 = []

    overall = 0

    for i in range(len(G)):
        for j in range(len(G[i])):
            G2.append( (i, G[i][j][0], -G[i][j][1]) )
            overall += G[i][j][1]
    res = Kruskal( G2 )

    mini = float('inf')
    finalRes = 0

    for i in range(len(res)):
        res[i] = (res[i][0], res[i][1], -res[i][2])
        finalRes += res[i][2]
        if res[i][2] < mini:
            mini = res[i][2]
    
    pos1 = 0
    pos2 = 0

    while pos1 < len(G2) and pos2 < len(res) and -G2[pos1][2] == res[pos2][2]:
        pos1 += 2
        pos2 += 1

    finalRes += -G2[pos1][2]
    
    return ((overall) // 2) - finalRes

G = [
[(1, 15), (2, 5), (3, 10) ],
[(0, 15), (2, 8), (4, 5), (5, 12)],
[(0, 5), (1, 8), (3, 5), (4, 6) ],
[(0, 10), (2, 5), (4, 2), (5, 11)],
[(1, 5), (2, 6), (3, 2), (5, 2) ],
[(1, 12), (4, 2), (3, 11) ] 
]

#print(lufthansa( G ))

runtests ( lufthansa, all_tests=True )