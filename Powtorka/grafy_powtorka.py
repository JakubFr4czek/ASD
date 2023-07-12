from queue import PriorityQueue

def dfs( G ):

    def DFSVisit(temp):

        print(temp)

        for i in range(len(G[temp])):

            if visited[G[temp][i][0]] == False:
                visited[G[temp][i][0]] = True
                DFSVisit(G[temp][i][0]) 

    visited = [False] * len(G)

    for i in range(len(G)):
        if visited[i] == False:
            visited[i] = True
            DFSVisit(i)

def bfs(G, v):

    visited = [False] * len(G)
    pq = PriorityQueue()

    pq.put(v)
    visited[v] = True

    while not pq.empty():

        temp = pq.get()
        print(temp)

        for i in range(len(G[temp])):
            if visited[G[temp][i][0]] == False:
                visited[G[temp][i][0]] = True
                pq.put(G[temp][i][0])           

def Dijkstra(G, v):

    distance = [float('inf')] * len(G)

    pq = PriorityQueue()

    pq.put( (0, v) )
    distance[v] = 0

    while not pq.empty():

        priority, temp = pq.get()

        for i in range(len(G[temp])):
            if priority + G[temp][i][1] < distance[G[temp][i][0]]:
                distance[G[temp][i][0]] = priority + G[temp][i][1]
                pq.put( (distance[G[temp][i][0]], G[temp][i][0]) )

    return distance

def Macierzify( G ):

    M = [ [float('inf' ) for j in range(len(G))] for i in range(len(G)) ]

    for i in range(len(G)):
        for j in range(len(G[i])):

            M[i][G[i][j][0]] = G[i][j][1]

    return M

def BellmanFord(G, v):

    distance = [float('inf')] * len(G)
    distance[v] = 0

    for i in range(len(G) - 1):

        for j in range(len(G)):
            for k in range(len(G[j])):
                if distance[j] + G[j][k][1] < distance[G[j][k][0]]:
                    distance[G[j][k][0]] = distance[j] + G[j][k][1]

    #Ujemne cykle
    for i in range(len(G)):
        for j in range(len(G[i])):
            if distance[i] + G[i][j][1] < distance[G[i][j][0]]:
                return []
    
    return distance

def FloydWarshall( G ):

    distance = Macierzify( G )

    for i in range(len(distance)):
        for j in range(len(distance)):
            for k in range(len(distance)):
                if distance[j][i] + distance[i][k] < distance[j][k]:
                    distance[j][k] = distance[j][i] + distance[i][k]

    return distance

G = [

    [(1,1), (2,2)],
    [(0,1), (4,7)],
    [(0,2), (3,3)],
    [(2,3), (7,10)],
    [(1,7), (5,5), (6,3)],
    [(4,5), (7,4)],
    [(4,3), (7,2)],
    [(3,10), (5,4), (6,2)]


]

print(Dijkstra(G, 0))
res = BellmanFord(G, 0)
x = FloydWarshall(G)

print(res)
for i in range(len(x)):
    print(x[i])