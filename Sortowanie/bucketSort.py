def selectionsort(tab):

    for i in range(len(tab)):

        temp = i

        for j in range(i + 1, len(tab)):

            if tab[temp] > tab[j]:
                temp = j

        
        tab[i], tab[temp] = tab[temp], tab[i]

def bucektSort( T ):

    mini = min(T)
    maxi = max(T)

    buckets = [[] for _ in range(5)] #5 - number of buckets

    step = (maxi - mini) / 5

    for i in range(len(T)):

        res = int((T[i] - mini) / step)
        
        if  (int((T[i] - mini) / step) - (T[i] - mini) / step) == 0 and res!=0:
            res-=1

        buckets[res].append(T[i])

    for i in range(len(buckets)):
        selectionsort(buckets[i])

    pos = 0

    for i in range(len(buckets)):
        for j in range(len(buckets[i])):
            T[pos] = buckets[i][j]
            pos+=1








arr = [9.8, 0.6, 10.1, 1.9, 3.07, 3.04, 5.0, 8.0, 4.8, 7.68]

bucektSort(arr)
print(arr)