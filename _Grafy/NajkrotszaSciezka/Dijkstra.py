from math import inf
from collections import deque

#Zlozonosc: O(ElogV)
#Najkrotsza sciezka w grafie wazonym, ale nie dopuszczamy ujemnych
#DAG trzeba posortowac topologicznie

#to jest prawdopodobnie bellman - ford
def Dijkstra(G, v):

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
                distance[G[temp][i][0]] = distance[temp] + G[temp][i][1]
                path[G[temp][i][0]] = temp
                queue.append(G[temp][i][0])
    
    print(distance)
    print(path)

G1 = [

    [(1,2), (3,4)],
    [(3,3), (2,3)],
    [(4,2)],
    [(2,3), (4,4)],
    []

]

G2 = [

    [(4,3), (1,3)],
    [(2,1)],
    [(3,3), (5,1)],
    [(1,3)],
    [(5,2)],
    [(3,1), (0,6)]
]

G3 = [

    [(1,2), (2,4)],
    [(2,3), (3,3)],
    [(4,4), (3,-1)],
    [(4,2)],
    []

]

G = [

    [(1,5)],
    [(4,9), (3,3)],
    [(1,-4), (0,3)],
    [(5,2), (4,3)],
    [(2,-1), (5,-5)],
    [(2,8), (0,9)]

]

Dijkstra(G, 0)


