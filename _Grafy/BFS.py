#Time: O(V + E)
#Space: O(V + E)

def AddEdge(G, pos, child):

    if len(G) == pos:
        G.append([])

    if child != -1:
        G[pos].append(child)


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

G = []

AddEdge(G, 0, 1)
AddEdge(G, 0, 2)
AddEdge(G, 1, 2)
AddEdge(G, 2, 0)
AddEdge(G, 2, 3)
AddEdge(G, 3, 3)


#print( G )
bfs(G, 2)