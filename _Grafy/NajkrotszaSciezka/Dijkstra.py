from math import inf
from collections import deque

#Zlozonosc: O(ElogV)
#Najkrotsza sciezka w grafie wazonym, ale nie dopuszczamy ujemnych
#Rasowy Dijkstra

def left(i):
    return 2*i + 1
def right(i):
    return 2*i + 2

def heapifyMin(T, pos, N):

    l = left(pos)
    r = right(pos)

    mini = pos

    if l < N and T[l][1] < T[mini][1]:
        mini = l

    if r < N and T[r][1] < T[mini][1]:
        mini = r
    
    if mini != pos:
        T[pos], T[mini] = T[mini], T[pos]
        heapifyMin(T, mini, N)

def Dijkstra(G, v):

    distance = [inf for _ in range(len(G))]
    path = [-1 for _ in range(len(G))]

    distance[v] = 0

    queue = deque()

    queue.append((v,0))


    while len(queue) > 0:

        temp = queue.popleft()
        temp = temp[0]
        heapifyMin(queue, 0, len(queue))
        #szukam krawedzi o najmniejszym czasie dojscia

        for i in range(len(G[temp])):
            if(distance[temp] + G[temp][i][1] < distance[G[temp][i][0]]):

                if distance[G[temp][i][0]] == inf:
                    queue.append((G[temp][i][0], G[temp][i][1]))
                    heapifyMin(queue, 0, len(queue)) 

                distance[G[temp][i][0]] = distance[temp] + G[temp][i][1]
                path[G[temp][i][0]] = temp

    print(distance)
    print(path)

G = [

    [(1,2), (3,4)],
    [(3,3), (2,3)],
    [(4,2)],
    [(2,3), (4,4)],
    []

]

Dijkstra(G, 0)
