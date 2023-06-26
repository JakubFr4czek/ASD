def frog( T ):

    dp = [(0, float('inf')) for i in range(len(T))]
    mini = [0] * len(T)
    dp[0] = (T[0],0)

    cnt = 1
    for i in range(len(T) - 2, -1, -1):

        if T[i] == 0:
            mini[i] = cnt
            cnt+=1
        else:
            cnt -= T[i]
            mini[i] = cnt
            cnt+=1
    #print(mini)

    for i in range(len(dp)):
        for j in range(1, dp[i][0] + 1):
            
            #print(dp[i][0] - j, mini[i])
            if i + j < len(dp) and dp[i][0] - j >= mini[i + j]:

                if dp[i][1] + 1 <= dp[i + j][1]:
                #if dp[i][0] - j + T[i + j] > dp[i + j][0]:
                    dp[i + j] = (max( dp[i + j][0], dp[i][0] - j + T[i + j] ), dp[i][1] + 1)
    print(dp)





T1 = [2, 1, 1, 3, 0, 0, 1, 0]
T2 = [3, 1, 2, 3, 0, 0, 0, 0]
T3 = [5, 5, 0, 0, 0, 0, 0, 0, 0, 0]
T4 = [1,2,5,0,0,7,5,3,1,2,3,9,0,0,0,0,0,5,3,0]

frog( T4 )