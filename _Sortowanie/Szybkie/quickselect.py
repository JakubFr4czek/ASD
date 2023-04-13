#avg: O(n)
#worst: O(n^2)

def partitionLomuto(T, l, p):

    pivot = p

    greater = l

    for i in  range(l, pivot):

        if T[i] <= T[pivot]:
            T[i], T[greater] = T[greater], T[i]
            greater += 1

    T[greater], T[pivot] = T[pivot], T[greater]

    return greater


def quickSelect(T, l, p, k):

    if l == p: return T[l]

    pivot = partitionLomuto(T, l, p)

    if k < pivot:
        return quickSelect(T, l, pivot - 1, k)
    elif k > pivot:
        return quickSelect(T, pivot + 1, p, k)
    else:
        return T[pivot]

T = [1,2,4,6,3,1,2,3,8,7,6,5,3,1,7,5,3,2,5,7,8,4]

for i in range(len(T)):

    print(quickSelect(T, 0, len(T) - 1, i), end=' ')