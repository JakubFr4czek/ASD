#Jak nie jest napisane, że graf jest spójny, to trzeba rozważyć dwa przypadki
#Graf spójny (każdą parę wierzchołków łączy ścieżka)


#Sprawdzic czy graf jest dwudzielny
#mozna BFS i mozna DFS

#dajemy dziecion kolory
#pierwszy na zielono
#dzieci na przeciwny
#patrzymy czy dzieci nie maja koloru, jak ma i ma ten sam to zwracam false

#TU TRZEBA UWAŻAĆ NA GRAF NIESPÓJNY
#TEN ALGORYTM TRZEBA URUCHOMIĆ DLA KAŻDEJ SPÓJNEJ
#POPRAWIĆ ALGORYTM!!!!!!!!!!!!!!!!!!!!!!!!!! O to powyzej^^^^^^^^^^6


def AddEdge(G, pos, child):

    if len(G) == pos:
        G.append([])

    if child != -1:
        G[pos].append(child)


def dwudzielny(G, v):

    if len(G) == 0: return

    queue = []
    visited = [False for _ in range(len(G))]
    color = [0 for _ in range(len(G))]

    queue.append(v)
    visited[v] = True
    color[v] = 1 # 0 - niepokolorowany, 1 - czerwony, 2 - zielony

    while len(queue) != 0:
        
        
        temp = queue.pop(0)

        for i in range(len(G[temp])):

            if visited[G[temp][i]] == False:
                queue.append(G[temp][i])
                visited[G[temp][i]] = True
                if color[v] == 1:
                    color[G[temp][i]] = 2
                else:
                    color[G[temp][i]] = 1

            else:
                if color[G[temp][i]] == color[v]:
                    return False
                
    return True

G = [[] for _ in range(4)]

AddEdge(G, 0, 3)
AddEdge(G, 0, 1)
AddEdge(G, 1, 2)

print(dwudzielny(G, 0))