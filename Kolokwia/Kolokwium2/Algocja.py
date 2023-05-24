from collections import deque

def solve(G, C):

    H = [ [] for i in range(len(G)) ]

    for i in range(len(C)):
        H[C[i]] = G[C[i]]

    isCity = [ 0 for i in range(len(G)) ]

    for i in range(len(C)):
        isCity[C[i]] = 1



    for i in range(len(C)):

        queue = deque()
        visited = [False] * len(G)

        #Zawsze na poczatku z miasta wychodza dwa
        queue.append(G[C[i]][0])
        queue.append(G[C[i]][1])
        visited[G[C[i]][0]] = True
        visited[G[C[i]][1]] = True

        while len(queue) > 0:

            temp = queue.popleft()
            print(temp)

            for j in range(len(G[temp])):

                if visited[G[temp][j]] == True:
                    continue

                if isCity[G[temp][j]] == 1:
                    H[C[i]].append(G[temp][j])
                else:
                    queue.append(G[temp][j])
                    visited[G[temp][j]] = True

    for i in range(len(H)):
        print(H[i])










E = [(0, 1), (1, 2), (2, 3), (3, 5), (4, 5), (4, 7), (5, 9), (3, 9), (1, 7), (0, 7), (7, 10), (10, 11),
     (1, 6), (6, 8)]
C = [0, 2, 9, 4, 10, 6]

vertexes = 12


G = [ [] for i in range(vertexes)]

for i in range(len(E)):
    G[E[i][0]].append(E[i][1])
    G[E[i][1]].append(E[i][0])

#for i in range(len(G)):
#    print(G[i])

solve(G, C)