from egzP7btesty import runtests 
from collections import deque()

def binary_search(T, left, right, key):

    if right > left: return None

    mid = (left + right) // 2

    if key < T[mid]:
        return binary_search(T, left, mid - 1, key)
    elif key > T[mid]:
        return binary_search(T, mid + 1, right, key)
    else: 
        return mid

def ogrod( S, V ):
    
    dp = [0] * len(S)
    searchTab = []

    for i in range(len(S)):

        res = binary_search(searchTab, 0, len(searchTab) - 1, S[i])

        if res == None:

            searchTa #drzewa pezwdzialowe

    return 0
    
S = [2, 3, 1, 1, 4, 1, 2, 4, 1]
V = [5, 3, 6, 6]

print(ogrod(S,V))

#runtests(ogrod, all_tests = True)