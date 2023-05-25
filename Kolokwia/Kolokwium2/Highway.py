from collections import deque
import heapq

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

def Kruskal(G, popcnt):

    heap = []

    for i in range(len(G)):
        heapq.heappush(heap, G[i])
        #Sortuje w kolejnosci [0], [1], [2] jesli chodzi o krotke

    for j in range(popcnt):
        heapq.heappop(heap)

    A = []
    parent = [i for i in range(len(G))]
    rank = [0 for _ in range(len(G))]

    while len(heap) > 0:
        
        temp = heapq.heappop(heap)

        k1 = findSet(parent, temp[1])
        k2 = findSet(parent, temp[2])

        if k1 != k2:
            A.append((temp[1], temp[2], temp[0]))
            Union(parent, rank, temp[1], temp[2])
    
    return A

def solve( G ):

    G2 = deque()

    for i in range(len(G)):

        for j in range(i + 1, len(G)):

            G2.append( (((G[i][0] - G[j][0]) ** 2 + (G[i][1] - G[j][1]) ** 2) ** 0.5, i, j) )

    #for i in range(len(G2)):
    #    print(G2[i])
    popcnt = 0

    mini = float('inf')
    minires = []

    while popcnt < len(G2):

        res = Kruskal(G2,popcnt)

        #for i in range(len(res)):
        #    print(res[i])
        if len(res) < len(G) - 1: #bo krawedzi bedzie n - 1
            break

        print(res[len(res) - 1][2] - res[0][2])

        if res[len(res) - 1][2] - res[0][2] < mini:
            mini = res[len(res) - 1][2] - res[0][2]
            minires = res

        popcnt+=1

    print(mini)

    for i in range(len(minires)):
        print(minires[i])

        
        

G = [(4, 4), (2, 3), (4.5, 0), (0, 0), (1, -1), (3, -2), (2, -4), (-1, 2), (-2, -2), (-4, 4), (-5, 0)]
solve(G)