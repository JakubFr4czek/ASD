from zad6testy import runtests
from collections import deque

def Bipartie( G ):

    G2 = [ [ 0 for j in range(len(G) * 2 + 2) ] for i in range(len(G) * 2 + 2)]

    for i in range(len(G)):
        for j in range(len(G[i])):
            G2[i][G[i][j] + len(G)] = 1

    for i in range(len(G)):
        G2[i + len(G)][len(G2) - 2] = 1 #t - koniec

    for i in range(len(G)):
        G2[len(G2) - 1][i] = 1 #s - poczatek

    return G2

    for i in range(len(G2)):
        print(G2[i])

def DFS( M, s, t):

    visited = [False] * len(M)
    path = [-1] * len(M)

    stack = deque()

    stack.append(s)
    visited[s] = True

    while len(stack) > 0:
        
        temp = stack.pop()

        if temp == t:
            return path
        
        for i in range(len(M[temp])):

            if M[temp][i] != 0 and visited[i] == False:
                path[i] = temp
                visited[i] = True
                stack.append( i )

    return path

def BFS( M, s, t):

    visited = [False] * len(M)
    path = [-1] * len(M)

    queue = deque()

    queue.append(s)
    visited[s] = True

    while len(queue) > 0:

        temp = queue.popleft()

        if temp == t:
            return path
        
        for i in range(len(M[temp])):

            if M[temp][i] != 0 and visited[i] == False:
                path[i] = temp
                visited[i] = True
                queue.append( i )

    return path

def binworker( G ):
    
    M = Bipartie( G )

    t = len(M) - 2
    s = len(M) - 1

    path = BFS(M, s, t)

    flow = 0

    while path[t] != -1:

        flow += 1

        curr = t
        prev = path[t]

        while prev != -1:

            M[prev][curr] = 0
            M[curr][prev] = 1

            curr = prev
            prev = path[curr] 

            path = BFS(M ,s, t)

    return flow

G = [ [ 0, 1, 3], # 0
[ 2, 4], # 1
[ 0, 2], # 2
[ 3 ], # 3
[ 3, 2] ] # 4

#print(binworker( G ))

runtests( binworker, all_tests = False )
