


def cycle_of_4(G):

    R = [ [ -1 for j in range(len(G)) ] for i in range(len(G))]

    for i in range(len(G)):

        for j in range(len(G[i])):
            for k in range(j):

                if R[G[i][j]][G[i][k]] == -1: #Pierwszy
                    R[G[i][j]][G[i][k]] = i
                else:
                    return G[i][j], G[i][k], R[G[i][j]][G[i][k]], i


G = [

    [1,2],
    [0,2],
    [0,1,3,5,8],
    [2,4],
    [3],
    [2,6,8],
    [5,7],
    [6,8],
    [2,5,7]

]

print(cycle_of_4(G))