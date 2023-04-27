#Time: O(V + E)
#Space: O(V + E)

def bfs(G, v):

    if len(G) == 0: return

    queue = []
    visited = [False for _ in range(len(G))]

    queue.append(v)
    visited[v] = True

    while len(queue) != 0:
        
        
        temp = queue.pop(0)
        print(temp, end=' ')

        for i in range(len(G[temp])):
            if visited[G[temp][i]] == False:
                queue.append(G[temp][i])
                visited[G[temp][i]] = True

G = [

    [1,2],
    [3,2],
    [4],
    [5],
    [5],
    [6,7],
    [],
    []

]

bfs(G, 0)