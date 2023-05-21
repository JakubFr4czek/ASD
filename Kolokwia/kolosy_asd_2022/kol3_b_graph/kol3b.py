from kol3btesty import runtests
from queue import PriorityQueue

def Dijkstra(G, v):

    distance = [float('inf') for _ in range(len(G))]
    path = [-1 for _ in range(len(G))]
    queue = PriorityQueue()

    distance[v] = 0
    queue.put((0, v))

    while not queue.empty():

        priotity, temp = queue.get()

        for i in range(len(G[temp])):

            if distance[G[temp][i][0]] > distance[temp] + G[temp][i][1]:
                distance[G[temp][i][0]] = distance[temp] + G[temp][i][1]
                queue.put((distance[G[temp][i][0]], G[temp][i][0]))
                path[G[temp][i][0]] = temp

    return distance



def airports( G, A, s, t ):
    
    G.append([])

    for i in range(len(G) - 1):
        G[i].append((len(G) - 1, A[i]))

    for i in range(len(A)):
        G[len(G) - 1].append((i,A[i]))

    dist = Dijkstra(G, s)
    return dist[t]

'''
G = [

    [(1,3), (3,2)],
    [(0,3), (2,20)],
    [(1,20),(5,1), (3,6)],
    [(0,2), (2,6), (4,1)],
    [(3,1), (5,7)],
    [(4,7), (2,1)]

]

A = [50, 100, 1, 20, 2, 70]

G.append([])

for i in range(len(G) - 1):
    G[i].append((len(G) - 1, A[i]))

for i in range(len(A)):
    G[len(G) - 1].append((i,A[i]))
'''
#for i in range(len(G)):
#    print(G[i])

#print(airports(G, A, 0, 5))

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( airports, all_tests = True )