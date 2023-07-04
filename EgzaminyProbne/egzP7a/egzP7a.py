from egzP7atesty import runtests 
from collections import deque

def CreateBipartiteGraph( T ):

    G = [ [ 0 for j in range(2 * len(T) + 2) ] for i in range(2 * len(T) + 2)] 

    for i in range(len(T)):
        G[len(T) + i][len(G) - 1] = 1
        for j in range(len(T[i])):
            if T[i][j] != None:
                G[i][T[i][j] + len(T)] = 1

    #filling source and sink
    for i in range(len(T)):
        G[len(G) - 2][i] = 1 #Source

    return G

def DFS(G, source, sink):

    visited = [False] * len(G)
    path = [-1] * len(G)

    stack = deque()
    stack.append(source)
    visited[source] = True

    while len(stack) > 0:

        temp = stack.pop()

        if temp == sink:
            return path

        for i in range(len(G[temp])):
            if G[temp][i] == 1 and visited[i] == False:
                path[i] = temp
                visited[i] = True
                stack.append(i)

    return None

def akademik( T ):
    
    ile_nonow = 0

    for i in range(len(T)):
        cnt = 0
        for j in range(len(T[i])):
            if T[i][j] == None:
                cnt+=1
        if cnt == 3:
            ile_nonow+=1

    #Konstruuje graf dwudzielny
    G = CreateBipartiteGraph( T )

    source = len(G) - 2
    sink = len(G) - 1
    #for i in range(len(G)):
    #    print(G[i])

    #print(DFS(G, len(G) - 2, len(G) - 1))

    path = DFS(G, source, sink)

    flow = 0

    while path != None:

        flow += 1

        curr = sink
        prev = path[curr]
        while prev != -1:

            G[prev][curr] = 0
            G[curr][prev] = 1

            curr = prev
            prev = path[curr]

        path = DFS(G, source, sink)

    return len(T) - (flow + ile_nonow)

T = [(2, 3, None), (0, 1, 3), (0, 2, None), (1, 3, 4), (2, 3, None)]
#akademik( T )


runtests ( akademik )