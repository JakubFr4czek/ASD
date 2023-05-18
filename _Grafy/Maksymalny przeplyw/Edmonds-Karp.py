from collections import deque


def BFS(M, v):

    queue = deque()
    visited = [False for _ in range(len(M))]
    path = [-1 for _ in range(len(M))]

    queue.append(v)
    visited[v] = True 
    
    while(len(queue) > 0):

        temp = queue.popleft()

        for i in range(len(M[temp])):
            if M[temp][i] > 0 and visited[i] == False:
                queue.append(i)
                visited[i] = True
                path[i] = temp
    #print(path)
    return path

def EdmondsKarp(M, s, t):

    flow = 0

    path = deque()
    path = BFS(M, s)

    while path[t] != -1:

        temp = t
        mini = float('inf')

        while temp != s:
            mini = min(mini, M[path[temp]][temp])
            temp = path[temp]
        temp = t

        while temp != s:
            M[path[temp]][temp] -= mini
            M[temp][path[temp]] += mini
            temp = path[temp]

        flow += mini

        path = BFS(M, s)
    return flow
        

G1 = [ #5

    [(1,3), (3,3)],
    [(2,4)],
    [(3,1), (4,2)],
    [(4,2), (5,6)],
    [(6,1)],
    [(6,9)],
    []

]

G2 = [ #26

    [(1,22), (3,4)],
    [(2,20), (3,7)],
    [(5,15)],
    [(4,18)],
    [(2,13), (5,20)],
    []

]

G = [ #200?

    [(1,100), (2,100)],
    [(2,1), (3,100)],
    [(3,100)],
    []

]

M = [ [0 for j in range(len(G))] for i in range(len(G))]

for i in range(len(G)):
    for j in range(len(G[i])):
        M[i][G[i][j][0]] = G[i][j][1]
        M[G[i][j][0]][i] = 0

#for i in range(len(M)):
#    print(M[i])

print(EdmondsKarp(M, 0, len(G) - 1))