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
    
T = [3,4,3,2,1,5,6,8,6,4,3,2,4,5,6,3,2,7,8,9,6,4,2,1,2,3,5,6,7,4,3]

print(quickSelect(T, 0, len(T) - 1, 7))




    

