#O(nlogn)
#niestabilny

def left(i):
    return 2*i + 1
def right(i):
    return 2*i + 2
def parent(i):
    return (i - 1)//2

def heapifyMin(T, pos, N):

    l = left(pos)
    r = right(pos)

    mini = pos

    if l < N and T[l] < T[mini]:
        mini = l

    if r < N and T[r] < T[mini]:
        mini = r
    
    if mini != pos:
        T[pos], T[mini] = T[mini], T[pos]
        heapifyMin(T, mini, N)

def heapsort( T ): 

    for i in range((len(T)//2)-1, -1, -1):
        heapifyMin(T, i, len(T))

    for i in range(len(T)-1, -1, -1):
        T[i], T[0] = T[0], T[i]
        heapifyMin(T, 0, i)

    