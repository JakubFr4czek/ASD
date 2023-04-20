#a[i] > a[j] and i < j
#da się zrobić w nlogn, podczas scalania

inwersje = 0

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
            global inwersje
            inwersje += (posTab - pos1)
        posTab +=1

    while pos1 < s1:
        tab[posTab] = arr1[pos1]
        pos1+=1
        posTab+=1

    while pos2 < s2:
        tab[posTab] = arr2[pos2]
        pos2+=1
        posTab+=1


tab = [4,3,2,1]

mergesort(tab, 0, len(tab) - 1)

print(inwersje)


