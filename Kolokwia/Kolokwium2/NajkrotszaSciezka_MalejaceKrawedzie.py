
def Solve(G, vertexes, s):

    distance = [float('inf') for _ in range(vertexes)]

    distance[s] = 0

    G.sort(key = lambda x : x[2], reverse = True)

    for u, v, w in G:

        if distance[u] < distance[v]:
            
            if distance[v] > distance[u] + w:
                distance[v] = distance[u] + w
        
        else:

            if distance[u] > distance[v] + w:
                distance[u] = distance[v] + w

    print(distance)

G = [

    (0,1,8),
    (0,2,9),
    (1,5,8),
    (2,4,1),
    (3,6,6),
    (4,2,6),
    (5,3,7),
    (1,4,1)

]

vertexes = 7 #0 - 6

Solve(G, vertexes, 0)
