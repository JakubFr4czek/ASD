from collections import deque
#Zlozonosc O(ElogV)
#Trzeba uzyc kolejki priorytetowej -> minHeap
#Tu bedzie spoko macierzowo zrobic

def left(i):
    return 2*i + 1

def right(i):
    return 2*i + 2

def heapifyMin(T, pos, N, distance):

    l = left(pos)
    r = right(pos)

    mini = pos

    if l < N and distance[T[l]] < distance[T[mini]]:
        mini = l

    if r < N and distance[T[r]] < distance[T[mini]]:
        mini = r
    
    if mini != pos:
        T[pos], T[mini] = T[mini], T[pos]
        heapifyMin(T, mini, N, distance)

#v - wierzcholek startowy
def Prim(M, v):

    distance = [float('inf') for _ in range(len(M))]
    parent = [-1 for _ in range(len(M))]
    queue = deque()

    #Dystans do samego siebie to 0
    distance[v] = 0
    queue.append(v) #Tak czy tak bedzie pierwszy

    #Umieszczam wszystkie wierzcholki w kolejce z odlegloscia inf
    for i in range(len(M)): #len(G) to liczba wierzcholkow, czyli O(v)
        if i != v:
            queue.append(i) #Tu i tak kazdy ma odleglosc inf, to nie trzeba heapify

    while len(queue) > 0:
        temp = queue.popleft()
        heapifyMin(queue, 0, len(queue), distance) #Tu nie wiem czy trzeba heapify

        for i in range(len(queue)):
            x = queue[i]
            if M[temp][x] < distance[x]:
                distance[x] = M[temp][x]
                parent[x] = temp
                heapifyMin(queue, 0, len(queue), distance)

    print(distance)
    print(parent)

G = [

    (0,1,1),
    (1,2,3),
    (0,4,4),
    (2,4,4),
    (0,5,8),
    (2,3,4),
    (4,5,7),
    (3,4,2)

]

maxi = -1

for i in range(len(G)):
    if G[i][0] > maxi:
        maxi = G[i][0]
    if G[i][1] > maxi:
        maxi = G[i][1]

maxi+=1

M = [ [ float('inf') for j in range(maxi)] for i in range(maxi)]

for i in range(len(G)):
    M[G[i][0]][G[i][1]] = G[i][2]
    M[G[i][1]][G[i][0]] = G[i][2]

Prim(M, 0)

