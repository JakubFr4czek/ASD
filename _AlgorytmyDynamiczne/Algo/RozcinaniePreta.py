

def pret(T, d):

    dp = [0] * d

    for i in range(len(T)):
        dp[T[i][0]] = T[i][1]

    for i in range(len(dp)):
        for j in range(len(T)):

            if T[j][0] <= i:

                if dp[T[j][0]] + dp[i - T[j][0]] > dp[i]:
                    dp[i] = dp[T[j][0]] + dp[i - T[j][0]]
                    
    print(dp)

T = [ (3,3), (1,1), (5,8), (7,12) ] #(dl, warotsc)
d = 18

print(pret(T, d))