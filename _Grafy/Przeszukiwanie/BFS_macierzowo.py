from collections import deque
#Macierzowo: O(V^2)

def BFS(G, v):

    visited = [False for _ in range(len(G))]
    path = [-1 for _ in range(len(G))]
    distance = [-1 for _ in range(len(G))]

    queue = deque()

    queue.append(v)
    visited[v] = True
    distance[v] = 0

    while len(queue) > 0:

        temp = queue.popleft()

        print(temp, end=' ')

        for i in range(len(G[temp])):

            if G[temp][i] == 1 and visited[i] == False:

                queue.append(i)
                visited[i] = True
                distance[i] = distance[temp] + 1
                path[i] = temp

    #print(visited)
    #print(path)
    #print(distance)

G = [

    [0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0]

]

BFS(G, 0)