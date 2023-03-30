#O(n^2)
#niestabilny

def selectionSort( T ):

    for i in range(len( T )):

        #szukam najmniejszego

        mini = i

        for j in range(i + 1,len(T)):
            if T[j] < T[mini]:
                mini = j

        T[i], T[mini] = T[mini], T[i]
