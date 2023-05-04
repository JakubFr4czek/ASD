
def left(i):
    return 2*i + 1

def right(i):
    return 2*i + 2

def heapifyMin(T, pos, N):

    l = left(pos)
    r = right(pos)

    mini = pos

    if l < N and T[l][1] < T[mini][1]:
        mini = l

    if r < N and T[r][1] < T[mini][1]:
        mini = r
    
    if mini != pos:
        T[pos], T[mini] = T[mini], T[pos]
        heapifyMin(T, mini, N)

'''def heapsort( T ): 

    for i in range((len(T)//2)-1, -1, -1):
        heapifyMin(T, i, len(T))

    for i in range(len(T)-1, -1, -1):
        T[i], T[0] = T[0], T[i]
        heapifyMin(T, 0, i)
'''

def Kruskal( G ):

    #Sortuje krawedzie po  wagach niemalejąco
    minHeap = []

    #Iteracja po wszystkich krawedziach O(E)
    for i in range(len(G)):
        for j in range(len(G[i])):
            minHeap.append(G[i][j])




G = [

    [(1,1), (4,4), (5, 8)],
    [(0,1), (2,3)],
    [(1,3), (4,4), (3,6)],
    [(2,6), (4,2)],
    [(0,4), (2,4), (3,2), (5,7)],
    [(0,8), (4,7)]

]