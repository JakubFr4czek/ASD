from collections import deque

def dfs(G, v):

    stack = deque()
    res = deque()
    visited = [False for _ in range(len(G))]

    stack.append(v)
    visited[v] = True

    while len(stack) > 0:

        temp = stack[len(stack)-1]
        #print(temp, end=' ') #bfs

        sth = False

        for i in range(len(G[temp])): #od tylu bo chce po najmniejszych

            if visited[G[temp][i]] == False:
                sth = True
                stack.append(G[temp][i])
                visited[G[temp][i]] = True
                break

        if sth == False:
            res.append(temp)
            stack.pop()

    for i in range(len(res)):
        print(res.pop(), end=' ')

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

dfs(G, 0)
