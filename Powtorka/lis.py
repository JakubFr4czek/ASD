
def lis( A ):

    dp = [1] * len(A)

    for i in range(len(A)):
        for j in range(i):
            if A[i] > A[j] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1

    print(dp)
    return max(dp)


A = [2,1,4,3,1,5,2,7,8,3]

print(lis(A))