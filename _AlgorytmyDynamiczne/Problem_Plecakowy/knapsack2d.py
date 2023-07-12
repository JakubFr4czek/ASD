
#h to wysokosc

def knapsack2d(P, W, H, c, h):

    dp = [ [ [0 for k in range(h + 1) ] for j in range(c + 1) ] for i in range(len(P))]

    for i in range(len(dp)):
        for j in range(c + 1):
            for k in range(h + 1):

                if i - 1 >= 0:
                    dp[i][j][k] = dp[i - 1][j][k]

                if i - 1 >= 0 and j - W[i] >= 0 and k - H[i] >= 0:
                    dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j - W[i]][k - H[i]] + P[i])

    return dp[len(dp) - 1][c][h]

P = [2, 1, 3, 7, 5, 1]
W = [8, 7, 3, 2, 9, 2]
H = [2, 1, 3, 4, 7, 2]

cap = 10
height = 10

print(knapsack2d(P, W, H, cap, height))