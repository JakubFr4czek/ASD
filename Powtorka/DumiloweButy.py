from queue import PriorityQueue

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

    print(path)
    return distance

def jumper( M ):

    G = [[] for i in range(len(M) * 2)]

    for i in range(len(M)):
        for j in range(len(M[i])):

            if M[i][j] != 0:
 
                G[i * 2].append( (j*2, M[i][j]) )
                G[i * 2 + 1].append( ((j*2, M[i][j])) )


                for k in range(len(M[j])):
                    if M[j][k] != 0:
                        G[i * 2].append( (2*k + 1, max(M[i][j], M[j][k])) )

    G[len(G) - 2].append((len(G), 0))
    G[len(G) - 1].append((len(G), 0))
    G.append( [] )#koniec t
    G.append( [(0,0), (1,0)] ) #poczatek s

    #for i in range(len(G)):
    #    print(G[i])

    #print("")

    

    dist = Dijkstra(G, len(G) - 1)

    #print(dist)
    print(dist[len(dist) - 2])
    

M = [
    [0,1,0,0,0],
    [0,0,1,0,0],
    [0,0,0,7,0],
    [0,0,0,0,8],
    [0,0,0,0,0]
]

jumper( M )