#odwracanie listy jednokierunkowej


class Node:

    def __init__(self, value, next = None):

        self.value = value
        self.next = next

def printList(head):

    while(head != None):
        print(head.value)
        head = head.next

def reverse(head):

    if head == None:
        return None
    if head.next == None:
        return head #????

    prev = None
    curr = head
    nxt = head.next

    while nxt != None:

        curr.next = prev
        prev = curr
        curr = nxt
        nxt = nxt.next

    curr.next = prev

    return curr



        



head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)

printList(head)
print(" ")

head = reverse(head)

printList(head)




