from kolutesty import runtests

def ice_cream( T ):

    T[0] = (T[0], 1)

    for i in range(1, len(T)):

        prevSum, off = T[i - 1]

        if T[i] - off > 0:
            T[i] = (prevSum + T[i] - off, off + 1)
        else:
            T[i] = T[i - 1]


    return T[len(T) - 1][0]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ice_cream, all_tests = False )
