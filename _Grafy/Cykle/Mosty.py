from math import inf


def Mosty(G, visited, v, processed, currProcessed, low, prev):

    for i in range(len(G[v])):

        if visited[G[v][i]] == False:
            
            visited[G[v][i]] = True

            processed[G[v][i]] = currProcessed
            currProcessed += 1

            Mosty(G, visited, G[v][i], processed, currProcessed, low, v)

    if prev == -1: #dla wierzcholka bez rodzica nie bedzie mostu
        return

    low[v] = processed[v]

    for i in range(len(G[v])):

        if G[v][i] != prev:

            if processed[G[v][i]] < low[v]:
                low[v] = processed[G[v][i]]
            
            if low[G[v][i]] < low[v]:
                low[v] = low[G[v][i]]

    if low[v] == processed[v]:
        print(prev, v)

G = [

    [1,2],
    [0,2,4],
    [0,6],
    [4,5],
    [1,3,5],
    [3,4],
    [2]

]

v = 0 #startowy wierzcholek

processed = [-1 for _ in range(len(G))] #czasy przetworzenia dla kazdego wierzcholka
processed[v] = 1
visited = [False for _ in range(len(G))]
visited[v] = True
low = [inf for _ in range(len(G))]

Mosty(G, visited, v, processed, 2, low, -1)