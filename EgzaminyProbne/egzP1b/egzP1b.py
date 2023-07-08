from egzP1btesty import runtests 
from queue import PriorityQueue

def Dijkstra(G, v):

    distance = [float('inf'), 0] * len(G)
    ity = [0] * len(G)
    path = [-1] * len(G)

    queue = PriorityQueue()

    distance[v] = 0
    queue.put((0, v))

    while not queue.empty():

        priotity, temp = queue.get()

        for i in range(len(G[temp])):

            if ity[temp] <= 3:

                if ity[G[temp][i]] == ity[temp]:

                    if distance[G[temp][i][0]] > priotity + G[temp][i][1]:
                        distance[G[temp][i][0]] = priotity + G[temp][i][1]
                        queue.put((distance[G[temp][i][0]], G[temp][i][0]))
                        path[G[temp][i][0]] = temp

                if ity[G[temp][i]] < ity

    return distance

def turysta( G, D, L ):

    G2 = [ [] for i in range(len(G)) ]

    for i in range(len(G)):
        e1, e2, w = G[i]
        G2[e1].append( (e2, w) )
        G2[e2].append( (e1, w) )

    res = Dijkstra(G2, D)

    print(res)

    return 0

G = [ 
(0, 1, 9), (0, 2, 1), 
(1, 2, 2), (1, 3, 8), 
(1, 4, 3), (2, 4, 7),
(2, 5, 1), (3, 4, 7), 
(4, 5, 6), (3, 6, 8), 
(4, 6, 1), (5, 6, 1) 
]

D = 0 
L = 6

turysta(G, D, L)

#runtests ( turysta )