
def binary_search(A, i, j, key):

    if i > j:
        return -1
    
    mid = (i + j) // 2

    if key < A[mid][0]:
        return binary_search(A, i, mid - 1, key)
    elif A[mid][0] < key:
        return binary_search(A, mid + 1, j, key)
    else:
        return mid

def solve(I, dp, res, pos, y):

    if dp[pos] != -1:
        return dp[pos]
    
    if I[pos][1] == y:
        return 1

    next = binary_search(I, pos, len(I) - 1, I[pos][1])
    
    if next == -1:
        return 0
    
    dp[next] = solve(I, dp, res, next, y)

    if dp[next] == 1:
        res.append(I[next])
        return 1
    else:
        return 0
    




def intuse(I, x, y):
    
    dp = [-1] * len(I) #Czy dolaczenie do przedzialu i-tego daje rozwiazanie,
    # -1 - nie sprawdzone, 0 - nie, 1 - tak
    res = []

    I.sort()
    
    start = binary_search(I, 0, len(I) - 1, x)

    if(start == -1): return None

    #Znaleziony
    x = solve(I, dp, res, start, y)

    if x == 1:
        res.append(I[start])

    print(x)

    print(res)

I = [ (3,4), (2,5), (1,3), (4,6), (1,4)]
x = 1
y = 6

intuse(I, x, y)