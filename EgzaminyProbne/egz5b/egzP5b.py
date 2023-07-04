from egzP5btesty import runtests 
from collections import deque

#punkty artykulacji

def koleje ( B ):
    
    #Preprocessing
    for i in range(len(B)): #O(n)
        if B[i][0] < B[i][1]:
            B[i] = (B[i][0], B[i][1])
        else:
            B[i] = (B[i][1], B[i][0])

    B.sort() #O(nlogn)

    res = deque()
    res.append(B[0])

    for i in range(1, len(B)):
        if B[i] != res[len(res) - 1]:
            res.append(B[i])
    #print(res)

    #Graphify
    G = [ [] for i in range(len(B)) ]

    for i in range(len(res)):
        G[res[i][0]].append(res[i][1])
        G[res[i][1]].append(res[i][0])

    print(G)

    return -1

B = [
    (3, 1), (0, 1), (4, 2), 
    (1, 2), (0, 1), (2, 4), 
    (2, 4), (0, 3), (2, 4), 
    (1, 0), (2, 1) 
]

print(koleje( B ))

#runtests ( koleje, all_tests=False )