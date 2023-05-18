

def Dfs_recursion(G, visited, v):

    print(v, end=' ')
    for i in range(len(G[v])):
        if visited[G[v][i]] == False:
            visited[G[v][i]] = True
            Dfs_recursion(G, visited, G[v][i])





visited = [False for _ in range(len(G))]

Dfs_recursion(G, visited, 0)