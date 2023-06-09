#4.  NWP (Najsluzszy wspolny podciag)
#- Ciag liczb A,B - n-elementowe
#- Podciag o najdluzszej dlugosci, taki ze jest podciagiem A oraz B
#A = [2, 7, 3, 5, 10, 7]
#B = [3, 4, 2, 7, 5, 7]
#Odp: 2,7,5,7
#
#S: Ta sama liczba i litera na i-tej(gora) i j-tej(lewo) pozycj to zwiekszam o 1 (Podobnie jak w szachownicy), tablica 2D (slowo A na gorze, a B na lewo)

def NWP(A, B):

    dp = [ [ 0 for j in range(len(B)) ] for i in range(len(A)) ]

    for i in range(len(A)):
        for j in range(len(B)):

            if i - 1 >= 0 and j - 1 >= 0:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            elif i - 1 >= 0:
                dp[i][j] = dp[i - 1][j]
            elif j - 1 >= 0:
                dp[i][j] = dp[i][j - 1]

            if A[i] == B[j]:
                dp[i][j] += 1

    return dp[len(A) - 1][len(B) - 1]

A = [5, 1, 2, 7, 3, 5, 10, 7]
B = [1, 3, 4, 2, 7, 5, 7]

print(NWP(A, B))
