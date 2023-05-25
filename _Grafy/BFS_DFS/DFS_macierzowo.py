#Macierzowo: O(V^2)

def DFS(G):

    def DFSVisit(G, v):

        nonlocal time
        time += 1

        visited[v] = True

        print("v: ",v," czas: ", time)

        for i in range(len(G[v])):

            if G[v][i] == 1 and visited[i] == False:
                path[i] = v
                DFSVisit(G,i)

        time += 1 #Tak jakos lepiej to liczy jak jest zakomentowane


    visited = [False for _ in range(len(G))]
    path = [-1 for _ in range(len(G))]

    time = 0 #czas przetworzenia wierzcholka

    for i in range(len(G)):

        if visited[i] == False:
            DFSVisit(G, i)

    #print(path)


G = [

    [0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]

]

DFS( G )