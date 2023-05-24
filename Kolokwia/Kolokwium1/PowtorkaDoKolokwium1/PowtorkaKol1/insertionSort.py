#O(n^2)
#stabilne

def insertionSort( T ):

    for i in range(1, len(T)):
            
            while T[i - 1] > T[i] and i > 0: #moge tak bo python nie psuje i z petli
                  
                  T[i - 1], T[i] = T[i], T[i - 1]
                  i-=1




T = [3,4,3,2,1,5,6,8,6,4,3,2,4,5,6,3,2,7,8,9,6,4,2,1,2,3,5,6,7,4,3] 

insertionSort(T)

print(T)