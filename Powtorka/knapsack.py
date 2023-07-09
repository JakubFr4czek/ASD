
def knapsack(P, W, C):

    dp = [ [ 0 for j in range(C + 1) ] for i in range(len(P) + 1) ]

    for i in range(1, len(dp)):
        for j in range(1, len(dp[i])):

            dp[i][j] = dp[i - 1][j]

            if j - W[i - 1] >= 0:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - W[i - 1]] + P[i - 1])

    for i in range(len(dp)):
        print(dp[i])


P = [1, 2, 5, 6]
W = [2, 3, 4, 5]
M = 8

print(knapsack(P, W, M))