from queue import PriorityQueue
#Do poprawy

def Prim(G, v):

    path = [-1 for _ in range(len(G))]
    distance = [ float('inf') for _ in range(len(G))]
    queue = PriorityQueue()

    distance[v] = 0
    queue.put(v, 0)

    while not queue.empty():
        temp = queue.get()

        for i in range(len(G[temp])):
            
            if G[temp][i][1] < distance[G[temp][i][0]]:
                
                if distance[G[temp][i][0]] == float('inf'):
                    distance[G[temp][i][0]] = G[temp][i][1]
                    queue.put(G[temp][i][0], distance[G[temp][i][0]])
                else:
                    distance[G[temp][i][0]] = G[temp][i][1]

                path[G[temp][i][0]] = temp

    return path    

G = [

    [(1,1), (4,5), (5,8)],
    [(0,1), (2,3)],
    [(1,3), (4,4), (3,6)],
    [(2,6), (4,2)],
    [(0,5), (2,4), (3,2), (5,7)],
    [(0,8), (4,7)]

]

print(Prim(G, 0))