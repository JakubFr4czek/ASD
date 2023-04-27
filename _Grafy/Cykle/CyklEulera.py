#Dziala tylko dla grafu spojnego i nieskierowanego
#ZlosonoscO(v+e) - listowo; O(v^2) - macierzowo

def r_Euler(G, visited, res, v):

    #print(v, end=' ')
    for i in range(len(G[v])):
        if visited[v][G[v][i]] == False:
            
            visited[v][G[v][i]] = True
            visited[G[v][i]][v] = True
            r_Euler(G, visited, res, G[v][i])

    res.append(v)

def Euler(G):

    #visited zawiera teraz odwiedzone krawedzie miast wierzcholkow
    #troche taka reprezentacja macierzowa, ale nie do konca
    visited = [ [ False for j in range(len(G)) ] for i in range(len(G))]
    res = []
    #print(visited)
    r_Euler(G, visited, res, 0)
    
    if(res[0] == res[len(res) - 1]):
        return res
    return []

G = [

    [1,2],
    [0,2,3,4,6],
    [0,1,3,4,5,6],
    [1,2,4,5],
    [1,2,3,5],
    [1,2,3,4],
    [1,2]


]

res = []
res = Euler(G)
print(res)