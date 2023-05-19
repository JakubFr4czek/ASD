from queue import PriorityQueue
#O(ElogV)


def Dijkstra(G, v):

    path = [-1 for _ in range(len(G))]
    distance = [float('inf') for _ in range(len(G))]
    queue = PriorityQueue()

    distance[v] = 0
    queue.put(v, 0)

    while not queue.empty():
        temp = queue.get()

        for i in range(len((G[temp]))):

            if distance[G[temp][i][0]] > distance[temp] + G[temp][i][1]:

                if distance[G[temp][i][0]] == float('inf'):
                    queue.put(G[temp][i][0], G[temp][i][1])

                distance[G[temp][i][0]] = distance[temp] + G[temp][i][1]
                path[G[temp][i][0]] = temp
            
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

print(Dijkstra(G, 0))