from egzP8btesty import runtests

def FloydWarshall( G ):


    dist = [ [float('inf') for j in range(len(G)) ] for i in range(len(G)) ]
    
    #Macierzify
    for i in range(len(G)):
        for j in range(len(G[i])):
            dist[i][G[i][j][0]] = G[i][j][1]

    #Zera na przekatnej
    for i in range(len(G)):
        dist[i][i] = 0

    #O(V^3)

    for i in range(len(dist)):
        for j in range(len(dist)):
            for k in range(len(dist)):

                if dist[j][i] + dist[i][k] < dist[j][k]:
                    dist[j][k] = dist[j][i] + dist[i][k]

    return dist

    
    for i in range(len(dist)):
        print(dist[i])



def robot( G, P ):

    dist = FloydWarshall(G)

    #for i in range(len(dist)):
    #    print(dist[i])

    res = 0

    prev = P[0]
    for i in range(1, len(P)):
        res += dist[prev][P[i]]
        prev = P[i]

    return res

G = [ 
 [(1, 3), (2, 3)], 
 [(0, 3), (4, 4)], 
 [(0, 3), (3, 1), (4, 4)], 
 [(2, 1), (4, 2)], 
 [(1, 4), (2, 4), (3, 2)] 
]

P = [0, 3, 4]

#print(robot(G,P))

runtests(robot, all_tests = True)
