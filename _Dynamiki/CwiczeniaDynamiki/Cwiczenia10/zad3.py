#- tablic A liczb naturalnych (Nie sa unikalne, ani posortowane), suma T
#- Czy mozna znalezc podzbior zbioru A, zeby sie zsumowal do T
#S: dp 2D, j to suma jaka mozna otrzymac, a i to suma od indeksow 0..i

def suma(A, T):

    dp = [ [False for j in range(len(A) + 1)] for i in range(T + 1) ]

    for i in range(len(A) + 1):
        dp[0][i] = True #zawsze da sie 0 stworzyc

    for i in range(1, T + 1):
        for j in range(1, len(A) + 1):

            if A[j - 1] <= i:

                reszta = i - A[j - 1]
                print(reszta)
                dp[i][j] = dp[i][j - 1] or dp[reszta][j - 1]
            else:
                dp[i][j] = dp[i][j - 1]

    for i in range(len(dp)):
        print(dp[i])

    print(max(dp[T]))

    #for i in range(1, T + 1):
    #    for j in range(len(A)):


A = [6, 2, 4]
T = 10

suma(A, T)