from collections import deque
#Listowo: O(E + V)
#Krawedzie odwiedzone w kazdym dfsvisit, tworza silnie spojna skladowa

def DFS_first(G): #Pierwszy, zwykly DFS

    def DFSVisit(G, v):

        nonlocal time
        time += 1

        visited[v] = True

        for i in range(len(G[v])):

            if visited[G[v][i]] == False:
                path[G[v][i]] = v
                DFSVisit(G,G[v][i])

        #Wierzcholek juz przetworzony
        time += 1
        processed.append(v)

    visited = [False for _ in range(len(G))]
    path = [-1 for _ in range(len(G))]
    processed = deque()

    time = 0 #czas przetworzenia wierzcholka

    for i in range(len(G)):

        if visited[i] == False:
            DFSVisit(G, i)

    return processed

def DFS_second(G, order): #SilnieSpojne skladowe

    def DFSVisit(G, v, id):

        visited[v] = True

        for i in range(len(G[v])):

            if visited[G[v][i]] == False:
                SilnieSpojne[G[v][i]] = id
                DFSVisit(G,G[v][i], id)

    visited = [False for _ in range(len(G))]
    SilnieSpojne = [-1 for _ in range(len(G))]

    id = 0

    for i in range(len(G)):

        if visited[order[i]] == False:
            SilnieSpojne[order[i]] = id #jak odpalam, to ten wierzcholek tez trzeba policzyc
            DFSVisit(G, order[i], id)
            id+=1

    return SilnieSpojne, id


def reverseEdges( G ): #Listowo

    H = [[] for _ in range(len(G))]

    for i in range(len(G)):
        for j in range(len(G[i])):
            H[G[i][j]].append(i)

    return H


def SilnieSpojneSkladowe( G ):

    order = [i for i in range(len(G))]

    processed = DFS_first(G)
    
    #odwracam krawedzie
    H = reverseEdges( G )

    order = deque()
    while len(processed) > 0:
        order.append(processed.pop())

    silnieSpojneSkladowe, id = DFS_second(H, order)

    G2 = [ [] for _ in range(id) ]

    for i in range(len(G)):
        for j in range(len(G[i])):
            
            v1 = i
            v2 = G[i][j]

            v1 = silnieSpojneSkladowe[i]
            v2 = silnieSpojneSkladowe[G[i][j]]

            if v1 != v2:

                G2[v1].append(v2)

    for i in range(len(G2)):
        print(G2[i])
    
    

G = [

    [1,3],
    [2,10],
    [3],
    [4],
    [2,5],
    [2],
    [5,9],
    [6],
    [7],
    [8],
    [0,9]

]

SilnieSpojneSkladowe(G)
