from queue import PriorityQueue
#O(ElogV)
#Poprawiony (Wreszcie)

def Dijkstra(G, P, d, v):

    distance = [float('inf') for _ in range(len(G))]
    path = [-1 for _ in range(len(G))]
    fuel = [0 for _ in range(len(G))]
    queue = PriorityQueue()


    distance[v] = 0
    fuel[v] = d
    queue.put((0, v))

    while not queue.empty():

        priotity, temp = queue.get()

        if P[temp] == 1:
            fuel[temp] = d

        for i in range(len(G[temp])):

            if G[temp][i] != -1:

                if distance[i] > distance[temp] + G[temp][i]:

                    if fuel[temp] - G[temp][i] >= 0:

                        fuel[i] = fuel[temp] - G[temp][i]
                        distance[i] = distance[temp] + G[temp][i]
                        queue.put((distance[i], i))
                        path[i] = temp
    print(path)
    return distance

def jak_dojade(G, P, d, a, b):

    res = Dijkstra(G, P, d, a)

    print(res)

    return res[b]

G = [[-1, 6,-1, 5, 2],
[-1,-1, 1, 2,-1],
[-1,-1,-1,-1,-1],
[-1,-1, 4,-1,-1],
[-1,-1, 8,-1,-1]]

P = [0,1,3]

Q = [0 for _ in range(len(G))]

for i in range(len(P)):
    Q[P[i]] = 1



jak_dojade(G, Q, 3, 0, 2)




