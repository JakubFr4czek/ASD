

def FloydWarshall( G ):

    #Przygotowanie macierzy

    distance = [ [float('inf') for j in range(len(G))] for i in range(len(G)) ]
    parent = [ [-1 for j in range(len(G))] for i in range(len(G)) ]

    #Wpisuje krawedzie do macierzy

    #Iteracja po pwszystkich krawedziach grafu O(E)
    for i in range(len(G)):
        for j in range(len(G[i])):
            if G[i][j] == 1:
                distance[i][j] = 1 
                parent[i][j] = i

    #Droga do samego siebie ustawiam na 0
    for i in range(len(distance)):
        distance[i][i] = 0
    
    #Skracanie Sciezek
    for i in range(len(distance)): #Chcemy to zrobic n-razy
        for j in range(len(distance)):
            for k in range(len(distance)):
                #if j != i and i != k: #Nie jestem pewny tego
                    if distance[j][i] + distance[i][k] < distance[j][k]:
                        distance[j][k] = distance[j][i] + distance[i][k]
                        parent[j][k] = parent[i][k]

    return distance





M = [
[0, 1, 1, 0],
[1, 0, 0, 1],
[1, 0, 0, 1],
[0, 1, 1, 0],
]
x = 0
y = 3
d = 2

dist = FloydWarshall(M)

for i in range(len(dist)):
     print(dist[i])