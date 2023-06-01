from kol2testy import runtests
from queue import PriorityQueue

# Autor rozwiazania - Jakub Fraczek
# Numer indeksu: 415014

# Zlozonosc obliczeniowa: O( V * E * log(E) )

# Opis algorytmu:
# Moj pomysl jest taki, ze sortuje krawedzie rosnaco po wagach,
# a nastepnie przesuwam sie oknem o rozmiarze dokladnie (V - 1),
# poniewaz tyle krawedzi bedzie zawierac drzewo rozpinajace dla danego 
# grafu G. Okno zapewnia warunek 'pieknosci'. Nastepnie dla zbioru (V-1)
# krawedzi uruchamiam algorytm Kruskala, ktory jesli zwroci drzewo rozpinajace
# jest ono rozwiazaniem (poniewaz poruszamy sie po posortowanej tablicy, pierwsze
# zwrocone MST, bedzie zarazem najmniejszym).


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

def Kruskal(queue, vertexCnt):

    A = []
    parent = [i for i in range(vertexCnt)]
    rank = [0 for _ in range(vertexCnt)]

    while not queue.empty():
        
        temp = queue.get()

        k1 = findSet(parent, temp[1])
        k2 = findSet(parent, temp[2])

        if k1 != k2:
            A.append((temp[1], temp[2], temp[0]))
            Union(parent, rank, temp[1], temp[2])
    
    return A


def beautree(G):
    #przerabiam G na liste krawedzi
    queue = []

    visited = [ [False for j in range(len(G))] for i in range(len(G)) ]

    #Pozbywam sie duplikatow krawedzi
    for i in range(len(G)):
        for j in range(len(G[i])):
            if visited[G[i][j][0]][i] == False:
                queue.append( (G[i][j][1], i, G[i][j][0]) )
                visited[i][G[i][j][0]] = True

    queue.sort() #na szczescie sortuje po pierwszej wartosci w krotce
    #print(queue)

    #print(len(queue) - (len(G) - 1))
    #for i in range(len())

    lastPos = len(G) - 1

    for i in range( len(queue) - (len(G) - 1)):

        temp = PriorityQueue()
        #print("kju: ")
        for j in range(i, lastPos + i):
            temp.put( queue[j] )
            #print(queue[j], end=' ')
        #print("\n")
        #Im wczesniej tym mniejsze wagi w mst
        res = Kruskal(temp, len(G))
        #print(res)
        if len(res) == len(G) - 1: #len(G) - 1 - liczba krawedzi w MST

            sum = 0
            for j in range(len(res)):
                sum += res[j][2]
            #print(sum)

            return sum
        
    return None #Drzewo nie istnieje

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( beautree, all_tests = True )


