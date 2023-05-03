from math import inf, log, exp
from collections import deque

def Bellman_Ford(G, v):

    distance = [inf for _ in range(len(G))] #Lista odleglosci od wierzcholka v do innych wierzcholkow
    path = [-1 for _ in range(len(G))] #trackback dla kazdego wierzcholka

    distance[v] = 0 #dystans wierzcholka do samego siebie to 0

    queue = deque()
    queue.append(v)

    while len(queue) > 0:

        #tutaj chyba wypada wziac wierzcholek do ktorego najblizej jest
        temp = queue.popleft()

        for i in range(len(G[temp])):

            if distance[temp] + G[temp][i][1] < distance[G[temp][i][0]]:

                if(distance[G[temp][i][0]] == inf):
                    queue.append(G[temp][i][0])

                distance[G[temp][i][0]] = distance[temp] + G[temp][i][1]
                path[G[temp][i][0]] = temp
                
    for i in range(len(distance)):
        print(exp(distance[i]), end=' ')
    print()
    print(path)


# BAT, USD ,AUD, HKD
PLN = [(0, 1), (1, 0.1217), (2, 4.1541), (3, 2.7498), (4, 0.5292), (5, 3.0483), (6, 2.5559), (7, 3.1110), (8, 4.5915), (9, 1.2300), (10, 4.6550), (11, 5.1805), (12, 0.1125), (13, 3.1030), (14, 0.1954), (15, 0.6160), (16, 3.0630), (17, 0.3916), (18, 0.4025), (19, 0.9292), (20, 2.3476), (21, 0.2138), (22, 1.1440), (23, 0.5160), (24, 0.0746), (25, 0.2289), (26, 0.2276), (27, 0.8235), (28, 0.9316), (29, 2.8254), (30, 5.0845), (31, 0.3101), (32, 0.6001), (33, 5.6205)]

CURR = [] #jednostka pln wzgledem waluty

for i in range(len(PLN)):

    CURR.append(1 / PLN[i][1])

G = []
G.append(PLN)

for i in range(1, len(CURR)):
    
    res = []

    for j in range(len(PLN)):

        if i != PLN[j][0]:
            res.append((PLN[j][0], CURR[i] * PLN[j][1]))

    G.append(res)

#for i in range(len(G)):
#    print(G[i])


#Graf zbudowany
#print(G)
#logarytmuje kursy

for i in range(len(G)):
    for j in range(len(G[i])):
        G[i][j] = (G[i][j][0], log(G[i][j][1]))

#print(G)



Bellman_Ford(G, 0)
#Dijkstra(G, 0)




