#Zlozonosc O(ElogV)
#Mozna heapsort zamienic na sort z lambda

def left(i):
    return 2*i + 1

def right(i):
    return 2*i + 2

def heapifyMin(T, pos, N):

    l = left(pos)
    r = right(pos)

    mini = pos

    if l < N and T[l][2] < T[mini][2]:
        mini = l

    if r < N and T[r][2] < T[mini][2]:
        mini = r
    
    if mini != pos:
        T[pos], T[mini] = T[mini], T[pos]
        heapifyMin(T, mini, N)

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

    #I. Sortuje krawedzie po  wagach niemalejąco

    #minHeap = G #Mozna skopiowac, zeby nie psuc grafu

    #Pierwszy krok heapsorta
    for i in range((len(G)//2)-1, -1, -1):
        heapifyMin(G, i, len(G))

    #II. A - zbiro pusty, przegladam w kolejnosci nierosnacej
    
    A = []

    #Przygotowuje strukture find/union
    parent = [i for i in range(len(G))]
    rank = [0 for _ in range(len(G))]

    while len(G) > 0:

        #rozpakowuje
        v1, v2, w = G[0]

        #2 krok heapsort
        G[0], G[len(G) - 1] = G[len(G) -1], G[0]
        G.pop()
        heapifyMin(G, i, len(G))

        k1 = findSet(parent, v1)
        k2 = findSet(parent, v2)
 
        if k1 != k2:

            A.append((v1, v2, w))
            Union(parent, rank, v1, v2)

    #III. Zwracam A

    return A


#Ten sam graf w wersji z lista sasiedztwa
'''G = [

    [(1,1), (4,4), (5, 8)],
    [(0,1), (2,3)],
    [(1,3), (4,4), (3,6)],
    [(2,6), (4,2)],
    [(0,4), (2,4), (3,2), (5,7)],
    [(0,8), (4,7)]

]
'''

G = [

    (0,1,1),
    (1,2,3),
    (0,4,5),
    (2,4,4),
    (0,5,8),
    (2,3,4),
    (4,5,7),
    (3,4,2)

]

print(Kruskal( G ))