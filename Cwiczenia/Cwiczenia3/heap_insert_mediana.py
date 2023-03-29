#wyciagam mediane z kopca

#dwa kopce 1 maks 1 min tyle samo elementow
#parami rozne, pasuje kazdy ze szczytow

#po wyjeci naprawiam kopiec

#gdzie jest mediana teraz

#na szczynie drugiej

#dowolny z nuch bierzemy mediane
#jesli rozne to wiekszego z nich

#INSERT

#dodajemy do patrzymy na topy < niz top to tu, wieksze niz top to tu

# a co jedli po środku
#jesli nie sa rowne to do tego co ma mniej

#zeby nie dopuscic do sytuacji gdy roznica > 1, zabranie z jednego i dolozenie drugiego


def heapifyMax(arr, size, pos):

    left = 2 * pos
    right = 2 * pos + 1

    maks = pos

    if left < size and arr[left] > arr[maks]:
        maks = left

    if right < size and arr[right] > arr[maks]:
        maks = right

    if maks != pos:
        arr[maks], arr[pos] = arr[pos], arr[maks]

        heapifyMax(arr, size, maks)

def heapifyMin(arr, size, pos):
    left = 2 * pos
    right = 2 * pos + 1

    min = pos

    if left < size and arr[left] < arr[min]:
        min = left

    if right < size and arr[right] < arr[min]:
        min = right

    if min != pos:
        arr[min], arr[pos] = arr[pos], arr[min]

        heapifyMin(arr, size, min)


def heapsort(arr):

    for i in range (len(arr)//2, -1, -1):
        heapifyMax(arr, len(arr), i)

    for i in range(len(arr) - 1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]

        heapifyMax(arr, i, 0)


arr = [2,5,7,3,2,3,1,7,4,2,7,4,2,1,5,7]

heapsort(arr)

print(arr)

#nlongn

minHeap = []
maxHeap = []

for i in range(len(arr)//2):
    maxHeap.append(arr[i])

for i in range(len(arr)//2, len(arr)):
    minHeap.append(arr[i])


for i in range (len(maxHeap)//2, -1, -1):
    heapifyMax(maxHeap, len(maxHeap), i)

for i in range (len(minHeap)//2, -1, -1):
        heapifyMin(minHeap, len(minHeap), i)

print(minHeap)

print(maxHeap)





    



