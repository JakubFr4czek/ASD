
def binary_search( T, p, l, key):

    if p > l: return -1

    mid = (p + l) // 2

    if key < T[mid]:
        return binary_search(T, p, mid - 1, key)
    elif key > T[mid]:
        return binary_search(T, mid + 1, l, key)
    else:
        return mid

def insert(T, key):

    T.append(float('inf'))

    i = 0

    while i < len(T) and T[i] <= key:
        i += 1
    print(i)

    for j in range(len(T) - 1, i, -1):

        T[j] = T[j - 1]

    T[i] = key



def k_chaotyczne( T ):

    A = []

    for i in range(len(T)):

        idx = binary_search(A, T[i])

        if idx == -1

    print(A)




T = [0, 2, 1.1, 2]

print(k_chaotyczne( T ))