#zliczam jedna zmienna ile odcinkow sie zaczalo, a druga ile sie skonczylo
#ile zaczelo sie przed jego poczatkiem i skonczylo sie przed koncem

#nie ma ograniczeń ze wszystko sie zaczyna i konczy w osobnych punktach (nierownosci ostre, nieostre itp.)

'''
        --------------14
     -----5  ------6    ------6
    ----4   --2 

'''

def partition(arr, l, p):

    pivot = p
    greater = l

    for i in range(l, pivot):

        if arr[i][0] <= arr[pivot][0]:

            arr[i], arr[greater] = arr[greater], arr[i]

            greater += 1

    arr[greater], arr[pivot] = arr[pivot], arr[greater] #podmieniam pivot na samym koncu

    return greater

def quicksortTuple(arr, l, p):

    if l >= p: return

    pivot = partition(arr, l, p)

    quicksortTuple(arr, l, pivot - 1)
    quicksortTuple(arr, pivot + 1, p)



def znajdz(arr):

    quicksortTuple(arr, 0, len(arr) - 1)

    




arr = [(0,0+4), (1,1+5), (8,8+2), (9,9+6), (4,4+14), (20, 20+6)]

znajdz(arr)

print(arr)