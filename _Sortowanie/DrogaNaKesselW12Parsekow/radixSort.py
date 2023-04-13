def countingSort(T, pos):

    C = [0 for _ in range(27)] #26 small leters + space at lowest value
    B = [0 for _ in range(len(T))]

    for i in range(len(T)):
        if pos >= len(T[i]):
            C[0]+=1
        else:
            C[ord(T[i][pos]) - 96]+=1

    for i in range(1, 27): #accumulating
        C[i] += C[i - 1]

    for i in range(len(T) -1, -1, -1):

        if pos >= len(T[i]):
            C[0] -=1
            B[C[0]] = T[i]
        else:
            C[ord(T[i][pos]) - 96]-=1
            B[C[ord(T[i][pos]) - 96]] = T[i]

    for i in range(len(T)):
        T[i] = B[i]

    #print(C)

def radixSort( T ):

    maks = -1

    for i in range( len(T) ):
        if len(T[i]) > maks:
            maks = len(T[i])

    for i in range(maks - 1, -1, -1):

        countingSort(T, i)

T = ["kot","pies","tok","ala","maska","kill"]

#heapsort(T)
radixSort(T)

print(T)
