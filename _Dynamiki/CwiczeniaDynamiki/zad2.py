#2. Wydawanie monet (Metoda zachlanna dziala, jesli nominaly sa przynajmniej 2x wieksze od siebie, tutaj nie mozna)
#- N = [] tablica nominalow
#- T - kwota do wydania
#- inf monet kazdego nominalu
#- wydac T, aby uzyc jak najmniej monet

def change(N, T):

    dp = [ [ float('inf') for j in range(len(N) + 1) ] for i in range(T + 1) ]

    #kolumny to mozliwe reszty
    #wiersze to kolejne mozliwe wartosci 1..T

    for j in range(1, len(dp)):
        for i in range(1, len(dp[j])):
            
            r = j - N[i - 1]
            koszt = 0

            if r > 0:
                koszt = dp[r][i]

            if i - 1 >= 0:

                dp[j][i] = min(dp[j][i - 1], 1 + koszt)

            else:

                dp[j][i] = 1 + koszt


    #for i in range(len(dp)):
    #    print(dp[i])

    return min(dp[T])




N = [1, 4, 7, 11]
T = 34

print(change(N, T))