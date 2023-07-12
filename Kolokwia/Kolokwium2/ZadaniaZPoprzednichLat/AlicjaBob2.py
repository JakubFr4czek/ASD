from queue import PriorityQueue

def Dijkstra(G, v, AliceBob):

    distance = [float('inf')] * len(G)

    pq = PriorityQueue()

    if AliceBob == 0:
        pq.put((0, v, 0))
    else:
        pq.put((0, v, 1))

    distance[v] = 0

    while not pq.empty():

        priority, temp, paying = pq.get()

        for i in range(len(G[temp])):

                if paying == 0:
                    if priority < distance[G[temp][i][0]]:
                        distance[G[temp][i][0]] = priority
                        pq.put( (distance[G[temp][i][0]], G[temp][i][0], 1) )
                else:
                    if priority + G[temp][i][1] < distance[G[temp][i][0]]:
                        distance[G[temp][i][0]] = priority + G[temp][i][1]
                        pq.put( (distance[G[temp][i][0]], G[temp][i][0], 0) )

    return distance



G = [

    [(1,2), (2,6), (3,5)],
    [(0,2), (2,10)],
    [(1,10), (0,6), (4,17)],
    [(0,5), (4,4), (5,2)],
    [(2,17), (3,4), (6,7), (5,11)],
    [(3,2), (6,10), (4,11)],
    [(4,7), (5,10)]

]

print(Dijkstra(G, 0, 1)) #0 - Bob, 1 - Alice