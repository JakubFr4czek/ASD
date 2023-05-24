from collections import deque


def DFS(G):

    def DFSVisit(G, v):

        nonlocal time
        time += 1

        visited[v] = True

        #print("v: ",v," czas: ", time)

        for i in range(len(G[v])):

            if visited[G[v][i][0]] == False:
                path[G[v][i][0]] = v
                DFSVisit(G,G[v][i][0])

        time += 1 #Tak jakos lepiej to liczy jak jest zakomentowane
        top.append(v)


    visited = [False for _ in range(len(G))]
    path = [-1 for _ in range(len(G))]
    top = deque()

    time = 0 #czas przetworzenia wierzcholka

    for i in range(len(G)):

        if visited[i] == False:
            DFSVisit(G, i)

    return top

def ModifiedDijkstra(G, topological):

    distance = [float('inf') for _ in range(len(topological))]
    path = [-1 for _ in range(len(topological))]

    distance[topological[0]] = 0

    for i in range(len(topological)):

        #Relaksuje tylko dzieci tego wierzcholka

        for j in range(len(G[topological[i]])):

            if distance[G[topological[i]][j][0]] > distance[topological[i]] + G[topological[i]][j][1]:
                distance[G[topological[i]][j][0]] = distance[topological[i]] + G[topological[i]][j][1]
                path[G[topological[i]][j][0]] = topological[i]

    return distance, path

G = [

    [(2,10), (1,100)],
    [(3,1)],
    [(1,1), (4,4)],
    [(4,1)],
    []

]

res = DFS(G) #trzeba odwrocic

topological = deque()
for i in range(len(res)):
    topological.append(res.pop())


dist, path = ModifiedDijkstra(G, topological)

print(path)
print(dist)