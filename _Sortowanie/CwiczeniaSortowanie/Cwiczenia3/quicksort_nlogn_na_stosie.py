def partition(tab, l, r): #zalozylismy ze funkcjie partition juz mamy

    pivot = r

    greater = l

    for i in range(l, pivot):

        if tab[i] <= tab[pivot]:
            tab[i], tab[greater] = tab[greater], tab[i] 
            greater+=1

    tab[greater], tab[pivot] = tab[pivot], tab[greater]  
            
    return pivot

#rekurencja ogonowa (z wykladu z asd 16.03.2023)
#cos co sie wywouje ostatnie w kodzie
#kompilator moze to zrealizowac tak zeby nie zapychac stosu wogole
#dobry kompilator moze to zamienic na pletle


#mam wrazenie, ze to bylo na wykladzie z asd
def quicksort_(tab, l, r): #liczba wywolan rekurencyjnych logn

    while(l < r):

        pivot = partition(tab, l, r)
        quicksort(tab, pivot + 1, r)
        r = pivot - 1


#logn na stosie
#quicksort wywoluje siebie jednokrotnie nie dwukrotnie
def quicksort(tab, l, r):

    while(l < r):

        pivot = partition(tab, l, r)

        if r - pivot > pivot - l:
            quicksort(tab, l, pivot -1)
            l = pivot + 1
        else:
            quicksort(tab, pivot + 1, r)

tab = [1,5,7,4,2,8,6,3,4]
quicksort(tab, 0, len(tab)-1)
print(tab)

