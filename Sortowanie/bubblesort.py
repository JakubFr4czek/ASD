def bubblesort(tab, asc):
    
    for i in range(len(tab)):
        for j in range(len(tab)):
            if tab[i] < tab[j]:
                tab[i], tab[j] = tab[j], tab[i]