# 5.1 Najdluzszy podciag rosnacy
# A = [2, 7, 3, 5, 10, 7]
# Odp1: 2, 3, 5, 7
# Odp2: 2, 3, 5, 10
#
# S:(Algorytm LIS z wykladu) O(n^2)

def lis( A ):

    dp = [1] * len(A)

    for i in range(len(A)):
        for j in range(i):

            if A[j] < A[i] and dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1

    print(dp)

A = [2, 7, 3, 5, 10, 7]

lis(A)