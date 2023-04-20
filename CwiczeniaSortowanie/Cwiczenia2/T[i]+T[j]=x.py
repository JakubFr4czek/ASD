

def find(T, x):

    i = 0
    j = len(T) - 1

    while i < j:

        if T[i] + T[j] > x:
            j-=1
        elif T[i] + T[j] < x:
            i+=1
        else:
            return i,j
        
tab = [1,2,3,6,7,9,10,11,23,54]

print(find(tab, 15))

