

def heapify(tab, N, i):

    #ustawiam największy element do rodzica

    left = 2*i
    right = 2*i + 1

    maks = i

    if left < N and tab[left] > tab[maks]:
        maks = left
    
    if right < N and tab[right] > tab[maks]:
        maks = right

    if maks != i:
        tab[i], tab[maks] = tab[maks], tab[i]

        heapify(tab, N, maks)
        
    
def heapsort(tab):

    N = len(tab)

    for i in range((N//2) - 1, -1, -1):
        heapify(tab, N, i) 
    #teraz mam poprawnie zbudowany kopiec

    for i in range(N - 1, -1, -1):
        #print(tab)
        tab[0], tab[i] = tab[i], tab[0]

        heapify(tab, i, 0)

tab = [1,2,4,7,3,2,9,4,2,4,6]

heapsort(tab)