#trzeba z radixowac poprostu

def countSort( T ):

    N = len(T)

    C = [0 for _ in range(N)]
    B = [0 for _ in range(N)]

    for x in T:
        C[x%N] += 1

    for i in range(1, N):
        C[i] += C[i-1]

    for i in range(N -1, -1, -1):
        C[T[i]%N] -= 1
        B[C[T[i]%N]] = T[i]

    C = [0 for _ in range(N)]

    for x in T:
        C[x//N] +=1

    for i in range(1, N):
        C[i] += C[i-1]

    for i in range(N -1, -1, -1):
        C[T[i]//N] -= 1
        B[C[T[i]//N]] = T[i]

    
    

