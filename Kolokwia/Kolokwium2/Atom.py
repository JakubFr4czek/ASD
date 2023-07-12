from collections import deque


def print_arr(arr):
    for i in range(len(arr)):
        print(arr[i])

def Floyd_Warshall(G):

    distance = [[ float('inf') for j in range(len(G)) ] for i in range(len(G))]
    #parent = [[ -1 for j in range(len(G)) ] for i in range(len(G))]

    for i in range(len(G)):
        for j in range(len(G[i])):
            if G[i][j] != 0:
                distance[i][j] = G[i][j]
                #parent[i][j] = i

    for i in range(len(distance)):
        distance[i][i] = 0

    for i in range(len(distance)): #Chcemy to zrobic n-razy
        for j in range(len(distance)):
            for k in range(len(distance)):
                #if j != i and i != k: #Nie jestem pewny tego
                if distance[j][i] + distance[i][k] < distance[j][k]:
                    distance[j][k] = distance[j][i] + distance[i][k]
                    #parent[j][k] = parent[i][k]    

    #print_arr(parent)
    #print('\n', end='')
    #print_arr(distance)
    return distance


def Atom(M, x1, y1, d1):

    D = Floyd_Warshall(M)

    print_arr(D)

    visited = [ [False for i in range(len(M))] for j in range(len(M)) ]
    path = [ [(-1, -1) for i in range(len(M))] for j in range(len(M))]
    queue = deque()

    queue.append((x1, y1, (-1, -1)))

    while len(queue) > 0:

        x_pos, y_pos, parents = queue.popleft()

        if x_pos == parents[1] and y_pos == parents[0]:
            continue

        if x_pos == y1 and y_pos == x1:
            print((x_pos, y_pos), end=' ')

            x = parents[0]
            y = parents[1]

            while x != -1 and y != -1:

                print((x,y), end = ' ')

                x, y = path[x][y]
            #print((x_pos, y_pos))

            return True
        
        print(x_pos,y_pos)

        visited[x_pos][y_pos] = True
        if D[x_pos][y_pos] < d1:
            continue

        
        #print((x_pos, y_pos), parents)

        
        for i in range(len(D[x_pos])):

            for j in range(len(D[y_pos])):
                
                if i == x_pos or j == y_pos:
                    continue
                
                if M[x_pos][i] != 0 and M[y_pos][j] != 0:
                        if visited[i][j] == False:
                            path[i][j] = (x_pos, y_pos)
                            queue.append((i, j, (x_pos, y_pos)))
                elif M[x_pos][i] != 0:
                    if visited[i][y_pos] == False:
                        path[i][y_pos] = (x_pos, y_pos)
                        queue.append((i, y_pos, (x_pos, y_pos)))
                elif M[y_pos][j] != 0:
                    if visited[x_pos][j] == False:
                        path[x_pos][j] = (x_pos, y_pos)
                        queue.append((x_pos, j, (x_pos, y_pos)))
                




M1 = [

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

print(Atom(M1, x1, y1, d1), "OCHUJ")