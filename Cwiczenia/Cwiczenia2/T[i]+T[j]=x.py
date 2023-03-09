

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

