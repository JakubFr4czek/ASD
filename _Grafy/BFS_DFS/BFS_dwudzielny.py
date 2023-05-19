from collections import deque
#Listowo: O(E + V)

def Bipartite_BFS(G, v):

    visited = [False for _ in range(len(G))]
    color = [-1 for _ in range(len(G))]

    queue = deque()

    queue.append(v)
    visited[v] = True
    color[v] = 1

    while len(queue) > 0:
        
        temp = queue.popleft()

        #print(temp, end = ' ')

        for i in range(len(G[temp])):

            if visited[G[temp][i]] == False:

                queue.append(G[temp][i])
                visited[G[temp][i]] = True

                if color[temp] == 1:
                    color[G[temp][i]] = 2
                else:
                    color[G[temp][i]] = 1

            else:
                if color[G[temp][i]] == color[temp]:
                    return False
    return True

Gdwudzielny = [

    [1,2],
    [3],
    [3],
    [4,5],
    [6],
    [],
    []

]

Gniedwudzielny = [

    [1,2],
    [3],
    [1,3],
    [4,5],
    [6],
    [],
    []

]

print(Bipartite_BFS(Gdwudzielny, 0))