def insertionSort( T ):

    for i in range(1, len(T)):
            
            while T[i - 1] > T[i] and i > 0: #moge tak bo python nie psuje i z petli
                  
                  T[i - 1], T[i] = T[i], T[i - 1]
                  i-=1


def bucketSort( T ):

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
        insertionSort(buckets[i])

    pos = 0

    for i in range(len(buckets)):
        for j in range(len(buckets[i])):
            T[pos] = buckets[i][j]
            pos+=1


T = [0.6, 0.23, 0.54, 0.43, 0.64, 0.41, 0.98, 0.76]

bucketSort( T )
print(T) 