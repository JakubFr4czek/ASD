
#Problem plecakowy ciagly - mozna brac fragmenty przedmiotow

def knapsack(I, cap):

    #licze oplacalnosc dla kazdego przedmiotu
    P = []

    for value, weight in I:
         P.append( (value / weight, value, weight) )

    P.sort(reverse=True)

    i = 0

    while cap - P[i][2] >= 0:
        print(P[i], 1)
        cap -= P[i][2]
        i += 1
    
    print(P[i], cap/P[i][2])
        
    

    #print(P)
    

I = [ (5, 2), (4, 1), (12,7), (4, 3), (1, 3) ] #I - item, krotka (wartosc, waga)
capacity = 5

knapsack(I, 5)