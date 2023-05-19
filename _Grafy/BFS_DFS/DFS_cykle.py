#Listowo: O(E + V)
#To dziala tylko dla grafow nieskierowanych,
#dla skierowanych daje false positive

#Zwraca podwojny wynik, ale to raczej nie problem, bo wystarczy podzielic przez 2

def DFS(G):

    def DFSVisit(G, v):

        nonlocal time
        time += 1

        visited[v] = True

        print(v, end = ' ')

        for i in range(len(G[v])):

            if visited[G[v][i]] == False:
                path[G[v][i]] = v
                DFSVisit(G,G[v][i])
            else:
                if path[v] != G[v][i]:
                    print(path, v, G[v][i])

        time += 1 #Tak jakos lepiej to liczy jak jest zakomentowane


    visited = [False for _ in range(len(G))]
    path = [-1 for _ in range(len(G))]

    time = 0 #czas przetworzenia wierzcholka

    for i in range(len(G)):

        if visited[i] == False:
            DFSVisit(G, i)

    #print(path)

G = [

    [1,3],
    [0,2],
    [1,3,4],
    [0,2,4],
    [2,3,5, 6],
    [4,6],
    [4,5]

]

DFS( G )