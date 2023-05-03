#Cykl o dlugosci 4

#kazdy wypisany dwa razy

def Cycles(G, v):


    for i in range(len(G)): #Wybieram 1 wiersz

        for j in range(i + 1, len(G)): #Wybieram 2 wiersz
            
            ile = 0
            vert = []

            for k in range(len(G)): #Sprawdzam
                
                if k != i and k != j and G[i][k] == True and G[j][k] == True:
                    vert.append(k)

            if len(vert) > 1:
                print(i, j, vert)
                    

                        


G = [

    [1,2,7],
    [0,3,6],
    [0,3,4],
    [1,2,5,6],
    [2,5],
    [3,4,6],
    [1,3,5,8],
    [0],
    [6]

]

#reprezentacja listowa na macierzowa

M = [ [ False for j in range(len(G)) ] for i in range(len(G))]

for i in range(len(G)):
    for j in range(len(G[i])):
        M[i][G[i][j]] = True

#print(M)

Cycles(M, 0)