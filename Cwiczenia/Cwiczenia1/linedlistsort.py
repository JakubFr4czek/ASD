class Node:
    def __init__(self, value, next = None):
        self.value = value
        self.next = next

def insert(head:Node, ele:Node):

    if head == None:
        return ele

    tmp = head

    if tmp.value > ele.value:
        ele.next = tmp
        return ele

    while(tmp.next!=None):
        if tmp.next.value > ele.value:
            temp = tmp.next
            tmp.next = ele
            ele.next = temp
            return head
        tmp=tmp.next
    tmp.next = ele
    return head 

def printList(head:Node):

    while head!= None:
        print(head.value)
        head=head.next

def deleteMax(head:Node):

    if head == None:
        return None
    if head.next == None:
        return None
    
    temp = head
    maks = temp

    while temp.next != None:
        if temp.next.value > maks.value:
            maks = temp
        temp = temp.next
    if head.value > maks.next.value:
        head = head.next
    else:
        maks.next = maks.next.next

    return head

def Lsort(head):

    h1 = head
    h2 = None

    while h1 != None:
        temp = h1
        h1 = h1.next
        temp.next = None
        
        h2 = insert(h2,temp)
    return h2

#head = Node(2)
#head = insert(head, Node(1))
#head = insert(head, Node(3))
#head = insert(head, Node(5))
#head = insert(head, Node(4))
#head = insert(head, Node(4))

head = Node(3)
head.next = Node(1)
head.next.next = Node(4)
head.next.next.next = Node(2)

printList(head)

print(" ")

head = Lsort(head)

printList(head)




    