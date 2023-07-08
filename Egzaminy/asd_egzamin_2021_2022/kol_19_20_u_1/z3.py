from collections import deque

def binary_search(tab, i, j, key):

    if i > j: return -1

    mid = (i + j) // 2

    if key < tab[mid]:
        return binary_search(tab, i, mid - 1, key)
    elif key > tab[mid]:
        return binary_search(tab, mid + 1, j, key)
    else:
        return mid
    
def insert(tab, key):

    tab.append(float('inf'))

    for i in range(len(tab)):

        if key < tab[i]:
           
            j = len(tab) - 1
            while j > i:
                tab[j] = tab[j - 1]
                j -= 1
            tab[i] = key
            break



def longest_incomplete(A, k):

    #Robie tablice znanych wartosci
    W = []

    for i in range(len(A)):
        idx = binary_search(W, 0, len(W) - 1, A[i])

        if idx == -1:
            insert(W, A[i])

    #Bede sie poruszac oknem o rozmiarze k - 1
    C = [0] * len(W) 

    ile = k
    i = 0


    while i < len(A) and ile > 0:

        idx = binary_search(W, A[i])

        if C[idx] == 0:
            ile -= 1

        C[idx] += 1
        i += 1

    maxi = i - 1

    while i < len(A):

        if ile == 0:

            idx = binary_search(W, A[i])

            C[idx] -= 1

            if C[idx] == 0:
                ile += 1
        else:

            idx = binary_search(W, A[i])
            
            C[idx] == 0:
            ile += 1
            maxi = max(maxi, .....)



    print(W)


    
 



A = [1,100, 5, 100, 1, 5, 1, 5]

longest_incomplete(A, 3)