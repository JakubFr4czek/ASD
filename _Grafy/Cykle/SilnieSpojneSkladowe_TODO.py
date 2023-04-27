#Zlozonosc: O(V + E) - listowa, O(V^2) - macierzowa
#W grafie skierowanym tylko

def r_Dfs(G, v, visited, processed):

    print(v, end=' ')


    for i in range(len(G[v])):
        if visited[G[v][i]] == False:
            visited[G[v][i]] = True
            r_Dfs(G, G[v][i], visited, processed)

    processed[v] = processed[len(processed) - 1]
    processed[len(processed) - 1] += 1

def SilnieSpojneSkladowe( G ):

    #Robie dfs ze zliczaniem czasu przetworzenia

    visited = [False for _ in range(len(G))]

    processed = [-1 for _ in range(len(G) + 1)]
    processed[len(processed) - 1] = 1 #aktualna dlugosc processed

    for i in range(len(G)):



        if(visited[i] == False):
            visited[i] = True
            curr = r_Dfs(G, i, visited, processed)

    print(processed)

    #Odwracam krawędzie (zrobie sobie nowa liste)

    G2 = [[] for _ in range(len(G))]

    for i in range(len(G)):
        for j in range(len(G[i])):
            G2[G[i][j]].append(i)

    #print(G2)

    visited = [False for _ in range(len(G))]

    for i in range(len(processed))


    
    

G = [

    [1],
    [2],
    [0,3,8],
    [4,6],
    [5],
    [3],
    [5],
    [8],
    [9],
    [5,10],
    [7]

]

SilnieSpojneSkladowe( G )
    