#ciag z brakującymi elementem (wyszukiwanie binarne)

# 0 1 2 3 4 5 6 7 9

# -1 dla uporzadkowanego zbioru

def search(tab, l, p):

    if p <= l:
        if l == len(tab):
            return -1
        if tab[l] == l:
           return l + 1
        return l

    mid = (l + p)//2
    if tab[mid] == mid:

        return search(tab, mid + 1, p)
    
    else:

        return search(tab, l, mid - 1)
    




tab = [0,1,2,3,4,5,6,7,8,9]

print(search(tab, 0, len(tab)))