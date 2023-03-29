def is_pretty( num ): #O(n + k)

    arr = [0 for _ in range(10)]

    while num > 0:
        arr[num % 10]+=1
        num//=10
    
    jedno = 0
    wielo = 0

    for i in range(10):
        if arr[i] == 1:
            jedno += 1
        elif arr[i] > 1:
            wielo += 1

    return (jedno, wielo)

def prettyWeid_partition(T, l, r):#O(nlogn)

    pivot = r

    prettier = l

    for i in range(l, pivot):

        if T[i][1][0] > T[pivot][1][0]:
            T[i], T[prettier] = T[prettier], T[i]
            prettier += 1
        elif T[i][1][0] == T[pivot][1][0]:
            if T[i][1][1] > T[pivot][1][1]:
                T[i], T[prettier] = T[prettier], T[i]
                prettier += 1

    T[prettier], T[pivot] = T[pivot], T[prettier]

    return prettier

def prettyWeird_quicksort(T, l, r):

    if l >= r: return

    pivot = prettyWeid_partition(T, l, r)

    prettyWeird_quicksort(T, l, pivot - 1)
    prettyWeird_quicksort(T, pivot + 1, r)



def pretty_sort( T ):

    for i in range(len(T)):
        T[i] = (T[i], is_pretty(T[i]))

    prettyWeird_quicksort(T, 0, len(T) - 1)

    
    



T = [123, 1234, 3455, 76555]

pretty_sort(T)

print(T)