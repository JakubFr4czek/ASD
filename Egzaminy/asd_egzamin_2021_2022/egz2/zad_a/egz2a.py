from egz2atesty import runtests

def coal( A, T ):
    
    G = [T for i in range(len(A))]
    trace = [-1 for i in range(len(A))]

    for i in range(len(A)):

        for j in range(len(G)):
            if G[j] - A[i] >= 0:
                G[j] -= A[i]
                trace[i] = j
                break


    return trace[len(trace) - 1]

A = [1, 6, 2, 10, 8, 7, 1]
T = 10

print(coal(A, T))

# zmien all_tests na True zeby uruchomic wszystkie testy
#runtests( coal, all_tests = False )
