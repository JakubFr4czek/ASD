#avg: O(nlogn)
#worst: O(n^2)
#niestabilny    

def partitionLomuto(T, l, p):

    pivot = p #pivot na prawo, z prostego powodu (bo moge)

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

T = [3,4,3,2,1,5,6,8,6,4,3,2,4,5,6,3,2,7,8,9,6,4,2,1,2,3,5,6,7,4,3]

quicksort(T, 0, len(T) - 1)

print(T)



    
