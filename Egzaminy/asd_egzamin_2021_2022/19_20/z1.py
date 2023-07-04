from queue import PriorityQueue

def Dijkstra(G, s, t):

    dist = [float('inf')] * len(G)
    parent = [-1] * len(G) 

    pq = PriorityQueue()

    dist[s] = 0

    pq.put((0, s))

    while not pq.empty():

        pr, temp = pq.get()

        for i in range(len(G[temp])):

            if G[temp][i] != 0 and G[temp][i] != pr and dist[temp] + G[temp][i] < dist[i]:
                dist[i] = dist[temp] + G[temp][i]
                parent[i] = temp
                pq.put((G[temp][i], i))

    return dist[t]

    print(dist)
    print(parent)



    



G1 = [ [0,5,1,8,0,0,0 ],
[5,0,0,1,0,8,0 ],
[1,0,0,8,0,0,8 ],
[8,1,8,0,5,0,1 ],
[0,0,0,5,0,1,0 ],
[0,8,0,0,1,0,5 ],
[0,0,8,1,0,5,0 ] ]

print(Dijkstra(G1, 5, 2))
