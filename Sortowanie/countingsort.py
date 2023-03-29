
# stabilny counting sort
def countingSort( T ):

    maks = max(T) + 1

    C = [0 for _ in range(maks)] #nomalnie tutaj
    B = [0 for _ in range(len(T))]


    for i in range(len(T)):

        C[T[i]] += 1

    for i in range(1, maks): #ile elementow mniejszych
        C[i] += C[i - 1]
  
    for i in range(len(T)):
        C[T[i]]-=1
        B[C[T[i]]] = T[i]



    for i in range(len(T)):
        T[i] = B[i]


    
tab = [3,5,3,2,1,5,6,5,4,2,1,7,5,4,3,5,6,7,8,6,5,4,3,2,1,2,3,4,5,6,7,8,6,4]

countingSort(tab)

print(tab)

