#kth smallest #O(n) \ worst case O(n^2)

def partition(tab, l, r):

    pivot = r

    greater = l

    for i in range(l, pivot):

        if tab[i] <= tab[pivot]:
            tab[i], tab[greater] = tab[greater], tab[i] 
            greater+=1

    tab[greater], tab[pivot] = tab[pivot], tab[greater]  
            
    return greater

def quickSelect(T, l, p, k):

    if l == p: 
        return T[l]
    
    pivot = partition(T, l ,p)

    if k < pivot:
        return quickSelect(T, l, pivot - 1, k)
    elif k > pivot:
        return quickSelect(T, pivot + 1, p, k)
    else:
        return T[pivot]

def quickSort(T, l, p):

    if l >= p:
        return
    
    pivot = partition(T, l, p)

    quickSort(T, l, pivot - 1)
    quickSort(T, pivot + 1, p)

def section(T, p, q):

    first = quickSelect(T, 0, len(T) - 1, p)
    last = quickSelect(T, 0, len(T) - 1, q)

    arr = []

    for i in range(len(T)):
        if T[i] >= first and T[i] <= last:
            arr.append(T[i])
    print(arr)
    quickSort(arr, 0, len(arr) - 1)
    print(arr)
    return arr

T = [5,4,3,1,8,9,10,54,21,78,6]

arr = section(T,5,9)

#print(arr)



