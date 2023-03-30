#O(nlogn)
#stabilny (a przynajmniej w założeniu taki powinien być)

inversions = 0

def mergeSort(T, l, p):

    if l >= p: return

    pivot = (l + p)//2

    mergeSort(T, l, pivot)
    mergeSort(T, pivot + 1, p)

    #tu mam juz podzielone
    #lacze tablice od l:pivot i pivot+1:p

    arr1 = T[l:pivot + 1] #do pivot(bo ostatni not included)
    arr2 = T[pivot + 1:p + 1]

    p1 = 0
    p2 = 0
    pos = l #pozycja w T

    while p1 < len(arr1) and p2 < len(arr2):
        if arr1[p1] <= arr2[p2]:
            T[pos] = arr1[p1]
            p1+=1
            pos+=1
        else:
            T[pos] = arr2[p2]
            p2+=1
            pos+=1
            global inversions
            inversions += len(arr1) - p1

    while p1 < len(arr1):
        T[pos] = arr1[p1]
        p1+=1
        pos+=1
        
    while p2 < len(arr2):
        T[pos] = arr2[p2]
        p2+=1
        pos+=1

    return inversionsb

