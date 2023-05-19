#Zlozonosc: O(v!)

def r_Hamilton(G, visited, v, res):

    if(len(res) == len(G)): 
        return 1

    #print(v, end=' ')
    for i in range(len(G[v])):
        if visited[G[v][i]] == False:
            visited[G[v][i]] = True
            res.append(G[v][i])
            temp = r_Hamilton(G, visited, G[v][i], res)
            if temp == 1: return temp
            visited[G[v][i]] = False
            res.pop()
    
    return -1
    
def Hamilton( G ):

    for i in range(len(G)):

        visited = [False for _ in range(len(G))]
        res = []
        res.append(i)
        visited[i] = True
        r_Hamilton(G, visited, i, res)
        if(len(res) == len(G)):
            print(res)
            break #usuwajac to mozna sprawdzic czy z kazdego wierzcholka da sie przejsc wszystkie (powiedzmy ze to bedzie graf SuperHamiltonowski)


G = [

    [1,2],
    [0,2,3,4,6],
    [0,1,3,4,5,6],
    [1,2,4,5],
    [1,2,3,5],
    [1,2,3,4],
    [1,2]


]

Hamilton( G )
