
def klocki( A ):

    dp = [1] * len(A)

    for i in range(len(A)):
        A[i] = (A[i][0], -A[i][1])

    #Pierwsza rosnaco druga malejao
    A.sort(reverse = True)

    for i in range(len(A)):
        A[i] = (A[i][0], -A[i][1])

    print( A )

    for i in range(len(A)):
        for j in range(i):
            

            if A[j][0] >= A[i][0] and A[j][1] <= A[i][1]:
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1

    print(dp)


A = [ [2,3], [2,5], [1,4], [1,5], [6,10], [2,6], [3,11], [8,9], [7,9], [8,9] ]

print(klocki( A ))