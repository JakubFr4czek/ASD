#Wedrowka po szachownicy NxN
#-startowy w lewyn gornym, koncowy w prawym dolnym
#-kazde pole ma koszt, mozna sie poruszac w dol i prawo tylko
#-policzyc najtansza sciezke

def chess( M ):

    dp = [ [ M[i][j] for j in range(len(M[i]))] for i in range(len(M))]

    for i in range(len(M)):
        for j in range(len(M)):
            
            if i - 1 >= 0 and j - 1 >= 0:

                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + dp[i][j]

            elif j - 1 >= 0:

                dp[i][j] = dp[i][j - 1] + dp[i][j]

            elif i - 1 >= 0:

                dp[i][j] = dp[i - 1][j] + dp[i][j]
            
    #for i in range(len(dp)):
        #print(dp[i])

    return dp[len(M) - 1][len(M) - 1] 



M = [

    [1, 2, 1, 1],
    [2, 2, 1, 1],
    [2, 2, 1, 1],
    [2, 2, 2, 2]

]

print(chess(M))