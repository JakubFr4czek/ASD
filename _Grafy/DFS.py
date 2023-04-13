#Time: O(V + E)
#Space: O(V + E)

def AddEdge(G, pos, child):

    if len(G) == pos:
        G.append([])

    if child != -1:
        G[pos].append(child)


def DFS(G, v):

    if len(G) == 0: return

    visited = [False for _ in range(len(G))]

    stack = []

    stack.append(v)
    visited[v] = True

    while len(stack) != 0:

        temp = stack.pop()
        print(temp, end=' ')

        for i in range(len(G[temp]) - 1, -1, -1):

            if visited[G[temp][i]] == False:
                stack.append(G[temp][i])
                visited[G[temp][i]] = True


G = []

AddEdge(G, 0, 1)
AddEdge(G, 0, 2)
AddEdge(G, 1, 2)
AddEdge(G, 2, 0)
AddEdge(G, 2, 3)
AddEdge(G, 3, 3)

DFS(G, 0)