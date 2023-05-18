from collections import deque
#Listowo: O(E + V)

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

        #print(temp, end = ' ')

        for i in range(len(G[temp])):

            if visited[G[temp][i]] == False:

                queue.append(G[temp][i])
                visited[G[temp][i]] = True
                distance[G[temp][i]] = distance[temp] + 1
                path[G[temp][i]] = temp

    #print(visited)
    #print(path)
    #print(distance)

G = [

    [1,2],
    [3],
    [3],
    [4,5],
    [6],
    [],
    []

]

BFS(G, 0)