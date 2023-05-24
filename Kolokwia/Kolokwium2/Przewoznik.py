from queue import PriorityQueue

def Dijkstra(G, v, t):

    path = [-1 for _ in range(len(G))]
    queue = PriorityQueue()

    queue.put((-1 * float('inf'), v))

    while not queue.empty():

        priotity, temp = queue.get()

        priotity = priotity * -1

        for i in range(len(G[temp])):

            if G[temp][i][0] == t:
                return min(priotity, G[temp][i][1])
            
            queue.put( (-1 * min(priotity, G[temp][i][1]), G[temp][i][0]) )

    return None


G = [

    [(1,4), (2,2)],
    [(3,3),(4,4)],
    [(4,1)],
    [(5,3)],
    [(5,4)],
    []

]

print(Dijkstra(G, 0, 5))


