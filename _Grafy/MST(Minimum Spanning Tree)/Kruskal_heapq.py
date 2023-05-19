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

def Kruskal( G ):

    heap = []

    for i in range(len(G)):
        heapq.heappush(heap, G[i])
        #Sortuje w kolejnosci [0], [1], [2] jesli chodzi o krotke

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

G = [
    #value, v1, v2
    (1,0,1),
    (3,1,2),
    (5,0,4),
    (4,2,4),
    (8,0,5),
    (6,2,3),
    (7,4,5),
    (2,3,4)

]

print(Kruskal(G))