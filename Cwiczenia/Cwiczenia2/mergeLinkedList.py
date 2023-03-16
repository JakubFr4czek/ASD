class Node:

    def __init__(self, value, next = None):

        self.value = value
        self.next = next

def merge_linked_list(head1, head2):

    if head1.value > head2.value:

        temp = head1

        head2, head1 = head2.next, head2
        head1.next = temp
    res = head1

    while head1.next != None and head2 != None:
      
        if head1.next.value > head2.value:
            temp = head1.next
            head1.next = head2
            head2 = head2.next
            head1.next.next = temp
        head1 = head1.next

    if head2 != None:
        head1.next = head2

    return res

def printList(head):

    while head != None:
        print(head.value, end=' ')
        head = head.next

head1 = Node(2)
head1.next = Node(3)
head1.next.next = Node(4)
head1.next.next.next = Node(9)

head2 = Node(1)
head2.next = Node(7)

#printList(head1)
#printList(head2)

res = merge_linked_list(head1, head2)

printList(res)