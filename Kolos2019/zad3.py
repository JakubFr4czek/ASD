def mergesort(tab, l, p):
    if l>=p: return

    s = (l+p)//2
    
    mergesort(tab, l, s)    
    mergesort(tab, s + 1, p)

    #print(l, s, " ", s + 1, p)

    s1 = (s - l) + 1
    s2 = (p - (s+1)) + 1 

    arr1 = [0 for i in range(s1)]
    arr2 = [0 for i in range(s2)]

    for i in range(s1):
        arr1[i] = tab[i + l]
    for i in range(s2):
        arr2[i] = tab[s + 1 + i]
    
    #print(arr1, arr2)

    pos1, pos2, posTab = 0,0, l

    while pos1 < s1 and pos2 < s2:
        if arr1[pos1] <= arr2[pos2]:
            tab[posTab] = arr1[pos1]
            pos1+=1
        elif arr1[pos1] > arr2[pos2]:
            tab[posTab] = arr2[pos2]
            pos2+=1
        posTab +=1

    while pos1 < s1:
        tab[posTab] = arr1[pos1]
        pos1+=1
        posTab+=1

    while pos2 < s2:
        tab[posTab] = arr2[pos2]
        pos2+=1
        posTab+=1

def czy_suma(T, x):

    i = 0
    j = len(T) - 1

    while i < j:

        if T[i] + T[j] < x:
            i+=1
        elif T[i] + T[j] > x:
            j-=1
        else:
            return True
    return False 

def check( T ):

    mergesort(T, 0, len(T) - 1)

    for i in range(len(T)):

        print(czy_suma(T, T[i]))

T = [1,4,6,5,7,8,15,34,2,9,3]

check(T)