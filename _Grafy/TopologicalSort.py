def AddEdge(G, pos, child):

    if len(G) == pos:
        G.append([])

    if child != -1:
        G[pos].append(child)


def TopologicalSort(G):

    visited = [False for _ in range(len(G))]

    dfs_stack = []
    stack = []
    path = []

    for v in range(len(visited)):

        if visited[v] == True: continue

        dfs_stack.append(v)
        visited[v] = True

        while len(dfs_stack) != 0:

            temp = dfs_stack.pop()
            cnt = 0

            for i in range(len(G[temp]) -1 , -1 ,-1):

                if visited[G[temp][i]] == False:
                    cnt += 1
                    dfs_stack.append(G[temp][i])
                    visited[G[temp][i]] = True
            if cnt == 0:
                while len(path) != 0:
                    stack.append(path.pop())
                path.append(temp)


    for i in range(len(stack) - 1, -1 ,-1):
        print(stack[i], end = ' ')


G = [[] for _ in range(5)]

AddEdge(G, 0, 1)
AddEdge(G, 0, 2)
AddEdge(G, 1, 3)
AddEdge(G, 3, 4)

TopologicalSort( G )