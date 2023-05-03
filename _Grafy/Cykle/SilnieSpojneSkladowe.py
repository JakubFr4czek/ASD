#Zlozonosc: O(V + E) - listowa, O(V^2) - macierzowa
#W grafie skierowanym tylko
#Dla braku silnie spojnych skladowych, poprostu nic nie wypisuje

#Rekurencyjny Dfs
def r_Dfs(G, v, visited, processed):
    for i in range(len(G[v])):
        if visited[G[v][i]] == False:
            visited[G[v][i]] = True
            r_Dfs(G, G[v][i], visited, processed)

    processed[v] = processed[len(processed) - 1]
    processed[len(processed) - 1] += 1

def r_Dfs2(G, v, visited):

    if(visited[v] == True):
        print(v, end=' ')

    visited[v] = True

    for i in range(len(G[v])):
        if visited[G[v][i]] == False:
            visited[G[v][i]] = True
            r_Dfs2(G, G[v][i], visited)


def SilnieSpojneSkladowe( G ): #Robie dfs ze zliczaniem czasu przetworzenia

    visited = [False for _ in range(len(G))]

    processed = [-1 for _ in range(len(G) + 1)] #czasy przetworzenia dla kazdego wierzcholka
    processed[len(processed) - 1] = 1 #aktualna dlugosc processed

    for i in range(len(G)):

        if(visited[i] == False):
            visited[i] = True
            curr = r_Dfs(G, i, visited, processed)

    #Odwracam krawędzie (zrobie sobie nowa liste)

    G2 = [[] for _ in range(len(G))]

    for i in range(len(G)):
        for j in range(len(G[i])):
            G2[G[i][j]].append(i)
            
    visited = [False for _ in range(len(G))]

    processed.pop() #usuwam ostatni element przechowujacy aktualna wartosc processed

    #Sprawdzam dla wszystkich wierzcholkow
    while True:

        maxi = -1
        maxiVal = -1

        for i in range(len(processed)):

            if visited[i] == False and processed[i] > maxi:
                maxi = processed[i]
                maxiVal = i

        if maxi == -1:
            break

        r_Dfs2(G2, maxiVal, visited)
        print("")

        maxi = -1 
            


    
    

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

G2 = [

    [1],
    [2],
    [3],
    []

]

SilnieSpojneSkladowe( G )
    