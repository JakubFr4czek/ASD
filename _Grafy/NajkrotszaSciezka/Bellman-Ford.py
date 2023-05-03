from math import inf
from collections import deque

#Najkrotsza sciezka, ale dopuszcza ujemne (w przeciwienstwie do Dijkstry)
#Zlozonosc: O(VE)


def Bellman_Ford(G, v):

    #Inicjalizacja
    distance = [inf for _ in range(len(G))] #Lista odleglosci od wierzcholka v do innych wierzcholkow
    path = [-1 for _ in range(len(G))] #trackback dla kazdego wierzcholka
    distance[v] = 0 #dystans wierzcholka do samego siebie to 0

    #Relaksacja
    for i in range(len(G) - 1):
        
        #Dla kazdej krawedzi
        for j in range(len(G)):
            for k in range(len(G[j])):

                if(distance[j] + G[j][k][1] < distance[G[j][k][0]]):
                    distance[G[j][k][0]] = distance[j] + G[j][k][1]
                    path[G[j][k][0]] = j

    #Weryfikacja

    #Dla kazdej krawedzi
    for j in range(len(G)):
            for k in range(len(G[j])):
                if distance[j] + G[j][k][1] < distance[G[j][k][0]]:
                    return -1
                      

                
    
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

Bellman_Ford(G, 0)


