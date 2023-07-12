from queue import PriorityQueue

def Dijkstra(G, v):

    distance = [float('inf') for _ in range(len(G))]
    queue = PriorityQueue()

    distance[v] = 0
    queue.put((0,v, None))

    mini = float('inf')

    while not queue.empty():

        priority, temp, parent = queue.get()

        for i in range(len(G[temp])):
            
            if  i == parent or G[temp][i] == -1:
                continue

            if  priority + G[temp][i] < distance[i]:
                distance[i] = priority + G[temp][i]
                
                queue.put((distance[i], i, temp))
            else:
                #print(temp, G[temp][i][0], priority, distance[G[temp][i][0]], distance[G[temp][i][0]] + priority + G[temp][i][1])
                mini = min(mini, distance[i] + priority + G[temp][i])

    return mini

G = [
    [-1, 2, -1, -1, 1],
    [2, -1, 4, 1, -1],
    [-1, 4, -1, 5, -1],
    [-1, 1, 5, -1, 3],
    [1, -1, -1, 3, -1]
]

for i in range(len(G)):
    print(Dijkstra(G, i))