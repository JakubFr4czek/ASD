
def FloydWarshall_domkniecie( G ):

    #Przygotowanie macierzy

    G2 = [ [0 for j in range(len(G))] for i in range(len(G)) ]

    #Wpisuje krawedzie do macierzy

    #Iteracja po pwszystkich krawedziach grafu O(E)
    for i in range(len(G)):
        for j in range(len(G[i])):
            G2[i][G[i][j]] = 1

    for i in range(len(G2)):
        G2[i][i] = 1

    for i in range(len(G2)): #Chcemy to zrobic n-razy
        for j in range(len(G2)):
            for k in range(len(G2)):
               if G2[j][k] == 0:
                   if G2[j][i] == 1 and G2[i][k] == 1:
                       G2[j][k] = 1

    for i in range(len(G2)):
        print(G2[i])


G = [

    [1,2],
    [2],
    [0,3],
    []

]

FloydWarshall_domkniecie( G )
