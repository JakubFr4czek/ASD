#avg: O(nlogn)
#worst: O(n^2)
#niestabilny    

def partitionLomuto(T, l, p):

    pivot = p

    greater = l

    for i in range(l, pivot):
        if T[i] <= T[pivot]:
            T[i], T[greater] = T[greater], T[i]
            greater += 1
    T[greater], T[pivot] = T[pivot], T[greater]

    return greater

def quicksort(T, l, p):

    #eliminuje rekurencje ogonowa
    while l < p:
        pivot = partitionLomuto(T, l, p)
        quicksort(T, l, pivot - 1)
        l = pivot + 1