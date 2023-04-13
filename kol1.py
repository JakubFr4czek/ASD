
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
    
    C = [T[j] for j in range(i, i + p)]
    res = quickSelect(C, 0, p - 1, p - k)
    pivot = -1
    for j in range(len(T)):
        if T[j] == res:
            pivot = j

    print(T[pivot])
    i+=1

    while i + p - 1 < len(T):
        print(T[i - 1], T[i + p - 1])
        if T[i + p - 1] < T[i]:
            pivot+=1
        i+=1
        print(T[pivot])

T = [7, 9, 1,5,8,6,2,12]

k = 4
p = 5

print(ksum(T, k, p))
