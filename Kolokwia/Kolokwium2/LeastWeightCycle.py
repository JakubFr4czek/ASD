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
            
            if G[temp][i][0] == parent:
                continue

            if distance[G[temp][i][0]] > priority + G[temp][i][1]:
                
                distance[G[temp][i][0]] = priority + G[temp][i][1]
                queue.put((distance[G[temp][i][0]], G[temp][i][0], temp))
            else:
                #print(temp, G[temp][i][0], priority, distance[G[temp][i][0]], distance[G[temp][i][0]] + priority + G[temp][i][1])
                mini = min(mini, distance[G[temp][i][0]] + priority + G[temp][i][1])

    return mini
G = [

    [(1,6)],
    [(0,6), (2,2)],
    [(1,2), (3,5), (4,7)],
    [(2,5), (4,3)],
    [(2,7), (3,3)]

]

G2 = [

    [(4,1), (1,2)],
    [(3,1), (2,4), (0,2)],
    [(3,5), (1,4)],
    [(1,1), (4,4), (2,5)],
    [(0,1), (3,3)]

]

for i in range(len(G2)):

    res = Dijkstra(G2, i)
    print(res)