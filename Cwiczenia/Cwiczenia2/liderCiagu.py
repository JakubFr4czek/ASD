
#ustawiam pierwszy element na lidera i licznik na 1, jak kolejna wartos rozna
#to licznik -=1. jak licznik = -1 to ustalam nowego lidera

def lider(tab):

    cnt = 1
    lider = tab[0]

    for i in range(1,len(tab)):
        if tab[i] != lider:
            cnt -= 1
        if cnt == -1:
            lider = tab[i]

    return lider

tab = [1,2,5,3,5,5,5,5,3,2,6,5,5,3]

print(lider(tab))