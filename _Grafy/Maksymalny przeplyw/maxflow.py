from collections import deque

def DFS( G, s, t):


    visited = [False] * len(G)
    path = [-1] * len(G)

    stack = deque()

    stack.append(s)
    visited[s] = True

    while len(stack) > 0:
        
        temp = stack.pop()
        if temp == t:
            return path
        
        for i in range(len(G[temp])):
            if visited[G[temp][i][0]] == False:
                path[G[temp][i][0]] = temp
                visited[G[temp][i][0]] = True
                stack.append( G[temp][i][0] )

    return path

def FordFulkerson(G, s, t):

    path = DFS(G, s, t)
    

def maxflow(E, s):

    edges = -1

    for i in range(len(E)):
        edges = max(edges, max(E[i][0], E[i][1]))

    G = [[] for i in range(edges + 1)]

    for i in range(len(E)):
        G[E[i][0]].append((E[i][1], E[i][2]))
        G[E[i][1]].append((E[i][0], E[i][2]))

    N = len(G)

    G.append([]) #sink

    #kazdy wierzcholek z kazdym
    for i in range(N-1, -1, -1):
        G[i].append((N, float('inf')))
        for j in range(i):
            G[j].append((N, float('inf')))


            #for k in range(len(G)):
            #   print(G[k])
            
            FordFulkerson(G, s, N)
            
            G[j].pop()
        G[i].pop()

    


    



G = [

    (0,1,7),
    (0,3,3),
    (1,3,4),
    (1,4,6),
    (2,0,9),
    (2,3,7),
    (2,5,9),
    (3,4,9),
    (3,6,2),
    (5,3,3),
    (5,6,4),
    (6,4,8)

]

s = 2

print(maxflow(G, s))