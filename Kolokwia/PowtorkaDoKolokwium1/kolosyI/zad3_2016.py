class Node:
    def __init__(self, val):
        self.val = val # przechowywana liczba rzeczywista
        self.next = None # odsyłacz do nastepnego elementu

def insert(head, gagatek):

    temp = head
    prev = temp
    while temp != None:

        if temp.val > gagatek.val:
            prev.next = gagatek
            gagatek.next = temp
            break
        prev = temp
        temp = temp.next

def fixly(head):

    temp = head

    while temp.next != None:

        if temp.val > temp.next.val: #o tu jest gagatek

            gagatek = temp.next
            temp.next = temp.next.next
            break
        
        temp = temp.next

    print(gagatek.val)
    insert(head, gagatek)


def printList( head ):

    while head != None:
        print(head.val, end=' ')
        head = head.next


#1, 0, 3, 2, 4, 6, 5

head = Node(1)
head.next = Node(2)
head.next.next = Node(4)
head.next.next.next = Node(3)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = Node(7)

fixly(head)

printList(head)