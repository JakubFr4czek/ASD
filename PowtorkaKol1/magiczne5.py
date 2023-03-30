def insertionSort( T ):

    for i in range(1, len(T)):
            
            while T[i - 1] > T[i] and i > 0: #moge tak bo python nie psuje "i" z petli
                  
                  T[i - 1], T[i] = T[i], T[i - 1]
                  i-=1

def partitionLomuto(T, l, p, pivot):

    T[p], T[pivot] = T[pivot], T[p]
    pivot = p

    greater = l

    for i in  range(l, pivot):

        if T[i] <= T[pivot]:
            T[i], T[greater] = T[greater], T[i]
            greater += 1

    T[greater], T[pivot] = T[pivot], T[greater]

    return greater


def mediana(T, l , p):

    C = [T[l + i] for i in range((p - l) + 1)]
    #print(C)
    insertionSort(C)

    return C[len(C) // 2]

def znajdzMediane(T, l, p):

    if (p - l) + 1 <= 5:
        return mediana(T, l, min(l + 4, p))

    #dziele na 5

    arr = []

    for i in range(l, p + 1, 4):
        arr.append(mediana(T, i, min(i + 4, p)))

    return znajdzMediane(arr, 0, len(arr) - 1)
        

def znajdzPozycjePivota(T, l, p, x):

    for i in range(l, p + 1):
        if T[i] == x:
            return i


def magiczne5(T, l, p, k):

    if l == p: return T[l]

    x = znajdzMediane(T, l, p) #tu mam dopiero wartosc
    pivotPos = znajdzPozycjePivota(T, l, p, x)
    #print(l, p, pivotPos)
    pivot = partitionLomuto(T, l, p, pivotPos)

    if k < pivot:
        return magiczne5(T, l, pivot - 1, k)
    elif k > pivot:
        return magiczne5(T, pivot + 1, p, k)
    else:
        return T[pivot]

    

T = [1,2,4,6,3,1,2,3,8,7,6,5,3,1,7,5,3,2,5,7,8,4]

#print(magiczne5(T, 0, len(T) - 1, 15))

for i in range(len(T)):

    print(magiczne5(T, 0, len(T) - 1, i),end = ' ')

