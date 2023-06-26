from collections import deque #Do wypisywania

#Zwykle BST
#Mniejsza wartosc na lewo, wieksza na prawo
#Wartosci sie nie powtarzaja

class BSTNode:

    def __init__(self, key, data, parent):
        self.right = None
        self.left = None
        self.parent = parent
        self.key = key
        self.Data = data

class BST:
    
    def __init__(self, root):
        self.root = root

def BSTInsert(Tree, key, data):

    root = Tree.root

    while root != None:

        if key < root.key:
            if root.left == None:
                root.left = BSTNode(key, data, root)
                return
            else:
                root = root.left         
        elif key > root.key:
            if root.right == None:
                root.right = BSTNode(key, data, root)
                return
            else:
                root = root.right
        else:
            print("Execute order 66, user violated the rules of BST!")
            return

def search(Tree, key):

    root = Tree.root

    while root != None:

        if key == root.key:
            return root
        elif key < root.key:
            root = root.left
        else:
            root = root.right

    return None

def BSTMin(root):

    while root.left != None:
        root = root.left

    return root

def BSTMax(root):

    while root.right != None:
        root = root.right

    return root

def BSTPrint(Tree):

    root = Tree.root

    queue = deque()

    print(root.key)

    if root.left != None:
        queue.append(root.left)

    if root.right != None:
        queue.append(root.right)

    while len(queue) > 0:

        curr = queue.popleft()

        print(curr.key)

        if curr.left != None:
            queue.append(curr.left)
        
        if curr.right != None:
            queue.append(curr.right)

def BSTTransplant(Tree, node1, node2):

    if node1.parent == None:
        Tree.root = node2

    elif node1 == node1.parent.left:
        node1.parent.left = node2

    else: node1.parent.right = node2

    if node2 != None:
        node2.parent = node1.parent

def BSTRemove(Tree, key):

    root = search(Tree, key)

    if root.left == None:
        BSTTransplant(T, root, root.right)
    elif root.right == None:
        BSTTransplant(T, root, root.left)
    else:
        curr = BSTMin(root.right)

        if root.parent != curr:
            BSTTransplant(Tree, curr, curr.right)
            curr.right = root.right
            curr.right.parent = curr

        BSTTransplant(Tree, root, curr)
        curr.left = root.left
        curr.left.parent = curr

        

Tree = BST(BSTNode(50, None, None))

T = [44, 3, 7, 77, 49, 42, 5, 1, 68, 11]

for i in range(len(T)):
    BSTInsert(Tree, T[i], None)

BSTRemove(Tree, 77)

BSTPrint(Tree)




