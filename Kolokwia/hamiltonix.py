
def DFS(G):

    def DFSVisit(G, v, gate):

        visited[v] = True   

        flaga = False

        for i in range(len(G[v][gate])):

            if visited[G[v][gate][i]] == False:
                flaga = True
                visited[G[v][gate][i]] = True
                #print(G[v][gate][i])
                path.append(v)

                DFSVisit(G,G[v][gate][i], 1 - gate)

        if flaga == False:
            print(path)
            visited[path.pop()] = False


    visited = [False for _ in range(len(G))]
    path = []
    DFSVisit(G, 0, 0)
    print(path)

G = [ ([1],[2,3,4]),
([0],[2,5,6]),
([1,5,6],[0,3,4]),
([0,2,4],[5,7,8]),
([0,2,3],[6,7,9]),
([1,2,6],[3,7,8]),
([1,2,5],[4,7,9]),
([4,6,9],[3,5,8]),
([3,5,7],[9]),
([4,6,7],[8]) ]

DFS(G)
