#Listowo: O(E + V)

def DFS_first(G):

    def DFSVisit(G, v):

        nonlocal time
        time += 1 #Czas odwiedzenia

        visited[v] = True
        low[v] = time #czas przetworzenia nadany przez dfs
        

        for i in range(len(G[v])):

            if visited[G[v][i]] == False:
                path[G[v][i]] = v
                DFSVisit(G,G[v][i])

        time += 1 #Czas przerworzenia

    visited = [False for _ in range(len(G))]
    path = [-1 for _ in range(len(G))]
    low = [float('inf') for _ in range(len(G))]

    time = 0 #czas przetworzenia wierzcholka

    for i in range(len(G)):

        if visited[i] == False:
            DFSVisit(G, i)

    return low, path

def DFS_second(G, path, low):

    def DFSVisit(G, v):

        visited[v] = True   

        for i in range(len(G[v])):

            if visited[G[v][i]] == False:
                DFSVisit(G,G[v][i])

        #Wierzcholek przetworzony
        mini = low[v]

        if path[v] != -1:

            for i in range(len(G[v])):
                if G[v][i] != path[v]:
                    mini = min(mini, low[G[v][i]])

            if mini == low[v]:
                print(path[v], v)

            low[v] = mini


    visited = [False for _ in range(len(G))]

    for i in range(len(G)):

        if visited[i] == False:
            DFSVisit(G, i)

    return low, path

def Mosty( G ):

    path = []
    low = []

    low, path = DFS_first( G )#Pierwsze przejscie nadaje "DFS-ową kolejnosc i liczy rodzicow dla kazdego wierzcholka"

    DFS_second(G, path, low)


G = [

    [1,6],
    [0,2],
    [1,3,6],
    [2,4,5],
    [3,5],
    [3,4],
    [0,2,7],
    [6]

]

Mosty( G )