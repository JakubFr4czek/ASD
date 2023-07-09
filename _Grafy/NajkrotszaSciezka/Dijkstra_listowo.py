from queue import PriorityQueue
#O(ElogV)
#Poprawiony (Wreszcie)

def Dijkstra(G, v):

    distance = [float('inf') for _ in range(len(G))]
    path = [-1 for _ in range(len(G))]
    queue = PriorityQueue()

    distance[v] = 0
    queue.put((0, v))

    while not queue.empty():

        priotity, temp = queue.get()

        for i in range(len(G[temp])):

            if distance[G[temp][i][0]] > priotity + G[temp][i][1]:
                distance[G[temp][i][0]] = priotity + G[temp][i][1]
                queue.put((distance[G[temp][i][0]], G[temp][i][0]))
                path[G[temp][i][0]] = temp

    return distance


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

print(Dijkstra(G, 0))