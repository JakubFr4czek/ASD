from collections import deque

def FloydWarshall( G ):

    distance = [ [float('inf') for j in range(len(G))] for i in range(len(G))]

    for i in range(len(G)):
        for j in range(len(G[i])):
            if G[i][j] != 0:
                distance[i][j] = G[i][j]
            if i == j:
                distance[i][j] = 0

    for i in range(len(distance)):
        for j in range(len(distance)):
            for k in range(len(distance)):
                if distance[j][i] + distance[i][k] < distance[j][k]:
                    distance[j][k] = distance[j][i] + distance[i][k]
    return distance


def Atom(M, x1, y1, d):

    G = FloydWarshall(M)

    for i in range(len(G)):
        print(G[i])

    visited = [ [False for j in range(len(G)) ] for i in range(len(G)) ]
    path = [ [(-1,-1) for j in range(len(G))] for i in range(len(G))]
    queue = deque()

    queue.append( (x1, y1) )
    visited[x1][y1] = True

    while len(queue) > 0:

        x, y = queue.popleft()

        if x == path[x][y][1] and y == path[x][y][0]:
            continue

        if x == y1 and y == x1:

            print(x,y)

            x,y = path[x][y]

            while x!= -1 and y != -1:
                print(x,y)
                x,y = path[x][y]
            

            return path


        print(x,y)
        visited[x][y] = True

        for i in range(len(M[x])):
            for j in range(len(M[y])):
                
                if i == x or j == y:
                    continue

                if M[x][i] != 0 and M[y][j] != 0:

                    if G[i][j] >= d and visited[i][j] == False: 
                        path[i][j] = (x, y)
                        queue.append( (i,j) )

                elif M[x][i] != 0:

                    if G[i][y] >= d and visited[i][y] == False:
                        path[i][y] = (x, y)
                        queue.append( (i,y) )

                elif M[y][j] != 0:

                    if G[x][j] >= d and visited[x][j] == False:
                        path[x][j] = (x,y)
                        queue.append( (x,j) )
                        

               


M = [

    [0, 5, 1, 0, 0, 0],
    [5, 0, 0, 5, 0, 0],
    [1, 0, 0, 1, 0, 0],
    [0, 5, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 0]

]

x1 = 0
y1 = 5
d1 = 4

Atom(M, x1, y1, d1)
