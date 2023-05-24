from queue import PriorityQueue

def Dijkstra(G, v):

    distance = [ [ float('inf') for i in range(2) ] for j in range(len(G)) ]
    path = [ [ -1 for i in range(2                                          ) ] for j in range(len(G)) ]
    queue = PriorityQueue()

    queue.put((0, v, -1, 1))
    queue.put((0, v, -1, 0))

    while not queue.empty() > 0:

        priority, temp, parent ,driver = queue.get()
        print(priority, temp)


        if distance[temp][driver] > priority:
            distance[temp][driver] = priority
            path[temp][driver] = parent
            

            #if temp == 5:
            #    break

            for i in range(len(G[temp])):

                if G[temp][i] != -1:
                    if driver == 0:
                        queue.put((distance[temp][driver] + G[temp][i], i, temp, 1))
                    else:
                        queue.put((distance[temp][driver], i, temp , 0))

    print(path)
    print(distance)

G = [

    [-1, 2, 1, -1, -1, -1],
    [2, -1, 5, 2, -1, 10],
    [1, 5, -1 ,3, 4,-1],
    [-1, 2, 3, -1, 1, 6],
    [-1, -1, 4, 1, -1, -1],
    [-1, 10, -1, 6, -1, -1]

]


Dijkstra(G, 0)
