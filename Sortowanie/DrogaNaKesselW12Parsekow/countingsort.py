#O(n + k), gdzie n to dlugosc tablicy na wejsciu, a k to dlugosc tablicy do zliczania

def znajdzMaks( T ):

    maxi = T[0]

    for i in range(1, len(T) - 1):
        if T[i] > maxi:
            maxi = T[i]

    return maxi

def countingSort( T ):

    maxi = znajdzMaks( T )

    C = [0 for _ in range(maxi + 1)]
    B = [0 for _ in range(len(T))]

    #zliczam
    for i in range(len(T)):
        C[T[i]] += 1
    
    #akumuluje
    for i in range(1, len((C))):
        C[i] += C[i - 1]
    
    #sortuje

    for i in range(len(T)-1, -1, -1):
        C[T[i]]-=1
        B[C[T[i]]] = T[i]

    for i in range(len(T)):
        T[i] = B[i]