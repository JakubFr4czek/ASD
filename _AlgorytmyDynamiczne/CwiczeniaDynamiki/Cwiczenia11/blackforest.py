
#Pomysl jest taki ze maksymalizuje zysk dla danego pola

def BlackForest( F ):

    dp = [0] * len(F)

    dp[0] = F[0]

    for i in range(1, len(F)):

        if i - 2 >= 0:
            dp[i] = max(dp[i - 1], dp[ i - 2] + F[i])
        else:
            dp[i] = dp[i - 1]

    print(dp)

F = [10, 1, 1, 10]

BlackForest( F )