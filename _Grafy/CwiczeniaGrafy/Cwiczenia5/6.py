#Reprezentacja macierzowa
#To zadanie zaklada direct krawedz do wierzcholka, a nie sciezke

def find(G):

    i = 0
    j = 0

    while i < len(G) and j < len(G):

        if G[i][j] == True:
            i+=1
        else:
            j+=1

    #print(i)

    for k in range(len(G)):

        if k != i:

            if G[k][i] == False:
                return -1
    
    return i

G = [

    [2,3],
    [2],
    [],
    [2,5],
    [2],
    [2,3,6],
    [2]

]

M = [ [ False for j in range(len(G)) ] for i in range(len(G))]

for i in range(len(G)):
    for j in range(len(G[i])):
        M[i][G[i][j]] = True


print(find(M))