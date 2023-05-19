from collections import deque
#Listowo: O(E + V)
#Krawedzie odwiedzone w kazdym dfsvisit, tworza silnie spojna skladowa

def DFS(G, order, flaga): #order to lista ktora mowi w jakiej kolejnosci odwiedzic wierzcholki, flaga liczy silnie spojne

    def DFSVisit(G, v):

        nonlocal time
        time += 1

        visited[v] = True

        for i in range(len(G[v])):

            if visited[G[v][i]] == False:
                SilnieSpojne.append(G[v][i])
                path[G[v][i]] = v
                DFSVisit(G,G[v][i])

        #Wierzcholek juz przetworzony
        time += 1
        processed.append(v)

    visited = [False for _ in range(len(G))]
    path = [-1 for _ in range(len(G))]
    processed = deque()
    SilnieSpojne = deque()

    time = 0 #czas przetworzenia wierzcholka

    for i in range(len(G)):

        if visited[order[i]] == False:
            
            SilnieSpojne.append(order[i]) #jak odpalam, to ten wierzcholek tez trzeba policzyc
            DFSVisit(G, order[i])
            if(flaga):
                print(SilnieSpojne)
                SilnieSpojne = deque()

    return processed


def reverseEdges( G ): #Listowo

    H = [[] for _ in range(len(G))]

    for i in range(len(G)):
        for j in range(len(G[i])):
            H[G[i][j]].append(i)

    return H


def SilnieSpojneSkladowe( G ):

    order = [i for i in range(len(G))]

    processed = DFS(G, order, False)
    
    #odwracam krawedzie
    G = reverseEdges( G )

    order = deque()
    while len(processed) > 0:
        order.append(processed.pop())

    DFS(G, order, True)






G = [

    [1],
    [2],
    [0,3,7],
    [4,6],
    [5],
    [3],
    [5],
    [8],
    [5,9],
    [10],
    [7]

]

SilnieSpojneSkladowe( G )