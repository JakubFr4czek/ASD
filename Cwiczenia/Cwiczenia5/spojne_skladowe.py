#policzyć liczbę spójnych składowych grafu G
#Graf spójny (każdą parę wierzchołków łączy ścieżka)

#Taka reprezentacja grafu nazywa się lista sąsiedztwa

def AddEdge(G, pos, child):

    if len(G) == pos:
        G.append([])

    if child != -1:
        G[pos].append(child)


def DFS(G, v, visited):

    if len(G) == 0: return

    stack = []

    stack.append(v)
    visited[v] = True

    while len(stack) != 0:

        temp = stack.pop()
        #print(temp, end=' ')

        for i in range(len(G[temp]) - 1, -1, -1):

            if visited[G[temp][i]] == False:
                stack.append(G[temp][i])
                visited[G[temp][i]] = True

def spojne_skladowe( G ):

    visited = [False for _ in range(len(G))]

    cnt = 0

    for i in range(len(visited)):

        if visited[i] == False:

            DFS(G, i, visited)
            cnt+=1
    return cnt
        

G = []

AddEdge(G, 0, 1)
AddEdge(G, 0, 2)
AddEdge(G, 1, 2)
AddEdge(G, 2, 0)
AddEdge(G, 2, 3)
AddEdge(G, 3, 3)
AddEdge(G, 4, -1)

print(spojne_skladowe(G))