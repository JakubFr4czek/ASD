def partition(tab, l, r):

    pivot = r

    greater = l

    for i in range(l, pivot):

        if tab[i] <= tab[pivot]:
            tab[i], tab[greater] = tab[greater], tab[i] 
            greater+=1

    tab[greater], tab[pivot] = tab[pivot], tab[greater]  
            
    return greater
def quicksort(tab, l, r):

    if l >= r: return

    pivot = partition(tab, l, r)

    quicksort(tab, l, pivot - 1)
    quicksort(tab, pivot + 1, r)

T = [10, 21, 54, 78, 9]
quicksort(T, 0 ,len(T) - 1)
print(T)