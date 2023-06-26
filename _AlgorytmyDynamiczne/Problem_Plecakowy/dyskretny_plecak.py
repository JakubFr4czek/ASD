#Moge brac tylko po 1 z danych przedmiotow

def knapsack(W, P, c): #Weight(array), Price(array), capacity(variable)

    #Potrzebuje stworzyc tablice, gdzie rzedy to numery
    #przedmiotow, a kolumny to wartosci 0, 1, 2, ..., c - 1, c

    dp = [ [ 0 for j in range(c + 1) ] for i in range(len(P)) ]

    #Musi byc plus jeden, bo dla ostatniej wartosci tez chcemy sprawdzic
    #a iterujemy tak naprawde do c - 1, a po c tez chcemy, stad c + 1

    for i in range(len(dp)):
        for j in range(c + 1): #

            #defaultowo wartosc pola to zero, wiec nie ma co sie przejmowac jak warunkow nie przejdzie
            if i - 1 >= 0:
                dp[i][j] = dp[i - 1][j] #wczesniejsze maksimum dla danej pojemnosci obliczone z poprzednich wag

            if i - 1 >= 0 and j - W[i] >= 0:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - W[i]] + P[i]) #Obliczam nowe maksimum uwzgledniajac nowy przedmiot

    for i in range(len(dp)):
        print(dp[i])

    return dp[len(dp) - 1][c]


    



P = [1, 2, 5 ,6]
W = [2, 3, 4, 5]
c = 8

print(knapsack(W, P, c))