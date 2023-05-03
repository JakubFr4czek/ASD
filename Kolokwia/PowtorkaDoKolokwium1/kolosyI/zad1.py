class Node:
    def __init__(self, val):
        self.val = val # przechowywana liczba rzeczywista
        self.next = None # odsyłacz do nastepnego elementu

def selectionsort(tab):

    for i in range(len(tab)):

        temp = i

        for j in range(i + 1, len(tab)):

            if tab[temp] > tab[j]:
                temp = j

        
        tab[i], tab[temp] = tab[temp], tab[i]

#bucket sort 0 - 10
def bucketSort(head):

    temp = head

    buckets = [ [] for _ in range(10)]

    step = 1

    while temp != None:

        if temp.val / step == int(temp.val / step) and temp.val != 0:
            buckets[int(temp.val/step) - 1].append(temp.val)
        else:
            buckets[int(temp.val/step)].append(temp.val)
        temp = temp.next

    for i in range(len(buckets)):
        selectionsort(buckets[i])

    for i in range(len(buckets)):
        for j in range(len(buckets[i])):
            head.val = buckets[i][j]
            head = head.next

    



def sortList(head):

    bucketSort(head)



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

sortList(head)

printList(head)