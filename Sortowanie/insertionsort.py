'''

    Sprawdzam dwa obok siebie i zamieniam dopóki pierwszy wiekszy od drugiego.
    Idę od j = i, "lecę po j" do tyłu (do 0).

'''

def insertionsort(tab):

    N = len(tab)

    for i in range(N):

        j = i

        while j > 0 and  tab[j - 1] > tab[j]:
            tab[j], tab[j - 1] = tab[j - 1], tab[j]
            j -= 1


