#jednoczesny min/max

def minmax(tab):

    N = len(tab)

    min = tab[0]
    maks = tab[0]

    for i in range(N - 1):

        if tab[i] < tab[i - 1]:
            if tab[i] < min:
                min = tab[i]
            if tab[i - 1] > maks:
                maks = tab[i - 1]

    return min, maks



tab = [1,5,3,2,1,6,32,1,23,5,4,1,5,1,1,23,5,6,64,32,2]

print(minmax(tab))