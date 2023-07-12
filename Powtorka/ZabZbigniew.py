


def zab(pad, energy, T, dp):

    print(pad, energy)
    if dp[pad][energy] != float('inf'):
        return dp[pad][energy]

    mini = float('inf')

    if pad + energy >= len(T) - 1:
        print("ochuj")
        return 1

    for i in range(1, energy + 1):

        if pad + i < len(T):

            mini = min(mini, zab(pad + i, energy - i + T[pad + i], T, dp) + 1)

    dp[pad][energy] = mini

    return mini

#T = [2, 2, 1, 0, 0, 0]
#T = [5, 5, 0, 0 ,0 ,0 ,0, 0, 0, 0]
T = [2,5,2,0,0,0,0,2,1,0,0]

dp = [ [ float('inf') for j in range(sum(T) + 1) ] for i in range(len(T))]

print(zab(0, T[0], T, dp))
print(dp)