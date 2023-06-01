

def lis( A ):

    C = [1] * len(A)
    path = [-1] * len(A)

    for i in range(len(C)):
        for j in range(i):

            if A[i] > A[j] and C[j] + 1 > C[i]:
                C[i] = C[j] + 1
                path[i] = j
    #print(path)
    #print(C)
    return max(C)





A = [2,1,4,3,1,5,2,7,8,3] 

print(lis(A))