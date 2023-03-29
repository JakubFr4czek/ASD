
def left( i ):
    return 2*i + 1
def right( i ):
    return 2*i + 2

def heapifyMin(i, T, n):

    l = left(i)
    r = right(i)

    mini = i

    if l < n and T[l] < T[mini]:
        mini = l
    if r < n and T[r] < T[mini]:
        mini = r

    if mini != i:
        T[mini], T[i] = T[i], T[mini]
    
        heapifyMin(mini, T, n)

def heapifyMax(i, T, n):

    l = left(i)
    r = right(i)

    maxi = i

    if l < n and T[l] > T[maxi]:
        maxi = l
    if r < n and T[r] > T[maxi]:
        maxi = r

    if maxi != i:
        T[maxi], T[i] = T[i], T[maxi]
        heapifyMax(maxi, T, n)

def median( T, tab):

    N = len(T)

    for i in range(N - 1, -1, -1):
        heapifyMin(i, T, N)

    for i in range(N - 1, -1, -1):
        T[i], T[0] = T[0], T[i]
        heapifyMin(0, T, i)

    #tu mam malejaco posortowana tablice
    
    pos = 0

    for i in range(len(tab) - 1):
        for j in range(i + 1, len(tab[0])):
            tab[i][j] = T[pos]
            pos+=1

    for i in range(len(tab)):
        tab[i][i] = T[pos]
        pos+=1

    
    #bla bla


    for i in range(len(tab)):
        for j in range(len(tab[0])):
            print(tab[i][j], end=' ')
        print("\n",end='')



#tab = [[2,3,5],[7,11,13],[17,19,23]]
tab = [[5,3,2], [3,1,2], [2,9,7]]
arr = []
for i in range(len(tab)):
    for j in range(len(tab[0])):
        arr.append(tab[i][j])
        tab[i][j] = 0

median(arr, tab)
