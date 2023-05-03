#kopiec z linked lista

class Node:
    def __init__(self, val):
        self.val = val # przechowywana liczba rzeczywista
        self.next = None # odsyłacz do nastepnego elementu

def left( i ):
    return 2*i + 1
def right( i ):
    return 2*i + 2
def parent( i ):
    return (i-1)//2

def heapifyMinRep(i, T, n):

    i = parent(i)

    l = left(i)
    r = right(i)

    mini = i

    if l < n and T[l] < T[mini]:
        mini= l
    if r < n and T[r] < T[mini]:
        mini = r

    if mini != i:
        T[mini], T[i] = T[i], T[mini]
        heapifyMin(mini, T, n)

def heapifyMin(i, T, n):

    l = left(i)
    r = right(i)

    mini = i

    if l < n and T[l] < T[mini]:
        mini= l
    if r < n and T[r] < T[mini]:
        mini = r

    if mini != i:
        T[mini], T[i] = T[i], T[mini]
        heapifyMin(mini, T, n)


def sortH(p, k): #p - head, k - k-chaotyczna

    res = p

    minHeap = []

    head = p


    #poczatkowe pakowanie
    while k > 0 and head != None:
        minHeap.append(head.val)
        heapifyMinRep(len(minHeap) - 1, minHeap, len(minHeap))
        k-=1
        head = head.next
    

    while len(minHeap) > 0:

        p.val = minHeap[0]
        p = p.next
        minHeap[0], minHeap[len(minHeap) - 1] = minHeap[len(minHeap) - 1], minHeap[0]
        heapifyMin(0, minHeap, len(minHeap) - 1)

        if head!=None:
            minHeap[len(minHeap) - 1] = head.val
            heapifyMinRep(len(minHeap) - 1, minHeap, len(minHeap))
            head = head.next
        else:
            minHeap.pop()

    return res


def printList( head ):

    while head != None:
        print(head.val, end=' ')
        head = head.next

#1, 0, 3, 2, 4, 6, 5

head = Node(1)
head.next = Node(0)
head.next.next = Node(3)
head.next.next.next = Node(2)
head.next.next.next.next = Node(4)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = Node(5)

res = sortH(head, 4)

printList(res)

