
#Szukam korzenia
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

def OperacjeNaGrafie( G ):

    #Ustawiam parent na self
    parent = [i for i in range(len(G))]
    rank = [0 for _ in range(len(G))]

G = [

    [(1,2), (2,4)],
    [(2,3), (3,3)],
    [(3,-1), (4,4)],
    [(4,2)],
    []

]

OperacjeNaGrafie( G )