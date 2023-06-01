from kol1testy import runtests

#Jakub Fraczek
#Pomysl polega na tym, aby przechodzic oknem
#o szerokosci p po tablicy i w tym oknie wyszukiwac
#k-ty najwiekszy element od konca. 
#
#W algorytmie przechodze oknem po tablicy, a nastepnie
#wyszukuje k-ty najwiekszy element z wykorzystaniem algorytmu
#quickselect
#
#Zlozonosc czasowa:(n * p)
#Zlozonosc pamiecowa:O(p)

def partitionLomuto(T, l, p):

    pivot = p

    greater = l

    for i in  range(l, pivot):

        if T[i] <= T[pivot]:
            T[i], T[greater] = T[greater], T[i]
            greater += 1

    T[greater], T[pivot] = T[pivot], T[greater]

    return greater


def quickSelect(T, l, p, k): #O(p)

    if l == p: return T[l]

    pivot = partitionLomuto(T, l, p)

    if k < pivot:
        return quickSelect(T, l, pivot - 1, k)
    elif k > pivot:
        return quickSelect(T, pivot + 1, p, k)
    else:
        return T[pivot]

def ksum(T, k, p):

    i = 0

    sum = 0

    while i + p - 1 < len(T):#n - p
        
        C = [T[j] for j in range(i, i + p)] #O(p) #musze kopiowac, bo quickselect niszczy poczatkowa tablice
        sum += quickSelect(C, 0, p - 1, p - k)
        i+=1

    return sum

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True )
