'''
    Selection sort polega na wybraniu najmniejszej liczby z tablicy
    i zamienienie jej z pierwszym elementem i tak dalej

'''

def selectionsort(tab):

    for i in range(len(tab)):

        temp = i

        for j in range(i + 1, len(tab)):

            if tab[temp] > tab[j]:
                temp = j

        
        tab[i], tab[temp] = tab[temp], tab[i]