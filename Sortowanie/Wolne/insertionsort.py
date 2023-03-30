#O(n^2)
#stabilne

def insertionSort( T ):

    for i in range(1, len(T)):
            
            while T[i - 1] > T[i] and i > 0: #moge tak bo python nie psuje "i" z petli
                  
                  T[i - 1], T[i] = T[i], T[i - 1]
                  i-=1