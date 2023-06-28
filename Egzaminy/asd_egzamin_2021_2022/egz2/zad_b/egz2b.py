from egz2btesty import runtests
from collections import deque

def magic( C ):

    dp = [-1] * len(C)

    dp[0] = 0

    for i in range(len(C)):

        for j in range(1, len(C[i])):

            if C[i][j][1] > i: #nie cofamy sie, bo za to grozi smierc

                #Czy moge wziac sztabki
                #print("dokąd: ",C[i][j][1], "max dla tego pola: ",dp[C[i][j][1]], "max pola z ktorego przychodze", dp[i], "wyliczone", max(dp[C[i][j][1]], dp[i] + min(10, (C[i][0] - C[i][j][0]))))
                #print(dp[i], C[i][0], C[i][j][0])
                if dp[i] != -1:
                    
                    if C[i][0] - C[i][j][0] <= 10:
                        dp[C[i][j][1]] = max(dp[C[i][j][1]], dp[i] + min(10, (C[i][0] - C[i][j][0])))

        #print(i, dp)
    

    return dp[len(dp) - 1]

C = [[2, [5, 1], [1, 6], [1, 8]],
[2, [7, 2], [1, 4], [1, 2]], 
[89, [91, 3], [75, 8], [84, 6]],
[8, [6, 4], [10, 6], [7, 5]],
[4, [5, 5], [1, 7], [3, 5]],
[10, [11, 6], [0, 6], [4, 6]],
[1, [0, 7], [0, 7], [6, 7]],#6
[57, [51, 8], [45, 8], [50, 8]],#7
[2, [6, 9], [7, 9], [0, 9]],
[6, [3, -1], [8, -1], [1, -1]]]


#print(magic(C))
#ans: 11
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( magic, all_tests = True )
