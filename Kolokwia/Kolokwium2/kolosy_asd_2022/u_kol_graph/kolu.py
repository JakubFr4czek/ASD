from kolutesty import runtests

def DFS(G, res):

    def DFSVisit(G, v):

        nonlocal time
        time += 1

        visited[v] = True

        #print("v: ",v," czas: ", time)

        for i in range(len(G[v])):

            if visited[G[v][i]] == False:
                path[G[v][i]] = v
                DFSVisit(G,G[v][i])

        time += 1 #Tak jakos lepiej to liczy jak jest zakomentowane
        res.append(v)


    visited = [False for _ in range(len(G))]
    path = [-1 for _ in range(len(G))]

    time = 0 #czas przetworzenia wierzcholka

    for i in range(len(G)):

        if visited[i] == False:
            DFSVisit(G, i)

def swaps( disk, depend ):

    ans = []

    DFS(depend, ans)
    res = []
    for i in range(len(ans)):
        res.append(ans.pop())   

    print(res)

    curr = disk[res[0]]
    swap = 0
    for i in range(1, len(res)):
        if curr != disk[res[i]]:
            swap+=1
            curr = disk[res[i]]
    return swap
'''disk = ['A', 'A', 'B', 'B']
depends = [

    [2,3],
    [],
    [1,3],
    [1]

]'''
#print(swaps(disk, depends))

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( swaps, all_tests = False )

