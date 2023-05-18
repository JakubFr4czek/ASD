#Listowo: O(V + E)

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


G1 = [

    [1,2],
    [3,2],
    [4],
    [5],
    [5],
    [6,7],
    [],
    []

]

G = [

    [3],
    [0],
    [1,4],
    [2,4],
    [5,6],
    [6],
    []

]

DFS(G, 0)