def partition(tab, r, l):

    pivot = l

    greater = r

    for i in range(r, pivot):

        if tab[i] <= tab[pivot]:
            tab[i], tab[greater] = tab[greater], tab[i] 
            greater+=1

    tab[greater], tab[pivot] = tab[pivot], tab[greater]  
            
    return pivot
def quicksort(tab, l, r):

    if l >= r: return

    pivot = partition(tab, l, r)

    quicksort(tab, l, pivot - 1)
    quicksort(tab, pivot + 1, r)
