
def DFS(G):

    def DFSVisit(G, v):

        visited[v] = True

        for i in range(len(G[v])):

            if visited[G[v][i]] == False:
                DFSVisit(G,G[v][i])

        #print(v)
        nonlocal czas

        czasy[v] = czas
        czas += 1

    visited = [False for _ in range(len(G))]
    czasy = [-1] * len( G )
    czas = 1

    for i in range(len(G)):

        if visited[i] == False:
            DFSVisit(G, i)
    
    return czasy

def DFS2(G):

    def DFSVisit(G, v):

        visited[v] = True

        for i in range(len(G[v])):

            if visited[G[v][i]] == False:
                DFSVisit(G,G[v][i])

    visited = [False for _ in range(len(G))]

    ile_spojnych = 0

    for i in range(len(G)):

        if visited[i] == False:
            ile_spojnych += 1
            DFSVisit(G, i)
    
    return ile_spojnych


def SilnieSpojneSkladowe( G ):

    czasy = DFS(G)
    #print(czasy)

    #odwracam krawedzie

    G2 = [ [] for i in range(len(G)) ]

    for i in range(len(G)):
        for j in range(len(G[i])):
            G2[G[i][j]].append(i)

    return DFS2(G2)

G = [

    [1],
    [2],
    [0,3],
    [4,6],
    [5],
    [3],
    []

]

SilnieSpojneSkladowe( G )