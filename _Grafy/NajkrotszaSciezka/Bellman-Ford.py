#O(VE)


def Bellman_Ford(G, v):

    #I - Inicjalizacja
    distance = [float('inf') for i in range(len(G))]
    path = [-1 for i in range(len(G))]

    distance[v] = 0

    #II - Relaksacja kazdej kwaredzi len(G) - 1 razy

    for i in range(len(G) - 1):

        #Iteracja po kazdej krawedzi
        for j in range(len(G)):#j to jest moj rodzic
            for k in range(len(G[j])):  

                if distance[G[j][k][0]] > distance[j] + G[j][k][1]:
                    distance[G[j][k][0]] = distance[j] + G[j][k][1]
                    path[G[j][k][0]] = j

    #III - Weryfikacja ujemnych cykli, jesli sa to nie ma najmniejszej sciezki
    
    for i in range(len(G)):
        for j in range(len(G[i])):
            if distance[G[i][j][0]] > distance[i] + G[i][j][1]:
                return []

    return path




G = [

    [(1,1), (2,8)],
    [(3,1)],
    [(3,3)],
    [(4,4)],
    [(5,10)],
    [(6,8), (8,15)],
    [(8,1),(7,1)],
    [(8,1)],
    []

]

print(Bellman_Ford(G, 0))