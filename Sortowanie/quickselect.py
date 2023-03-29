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