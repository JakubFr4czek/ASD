def left(i):
    return 2*i + 1
def right(i):
    return 2*i + 2

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

T = [2]

T.append(1)
T.append(0)
T.append(5)

heapifyMin(T, 0, len(T))

print(T)