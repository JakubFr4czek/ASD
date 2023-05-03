def selectionSort( T ):

    for i in range(len( T )):

        #szukam najmniejszego

        mini = i

        for j in range(i + 1,len(T)):
            if T[j] < T[mini]:
                mini = j

        T[i], T[mini] = T[mini], T[i]












T = [3,4,3,2,1,5,6,8,6,4,3,2,4,5,6,3,2,7,8,9,6,4,2,1,2,3,5,6,7,4,3] 

selectionSort( T )

print(T)