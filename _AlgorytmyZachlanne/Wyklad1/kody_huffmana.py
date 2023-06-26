from queue import PriorityQueue
from collections import deque

#Algorytm zachlanny
#Tworzy kody Huffmana dla danych oraz i czestosci wystepowania
#Prefiksowa metoda kompresji bezstratnej

#Biore dwa najmniejsze lacze w calosc i mniejszy z nich po lewo, wiekszy po prawo
#Tworze nowy obiekt bez znaku o lacznej czestosci tych dwoch

class Node:

    def __init__(self, value, frequency):
        self.value = value
        self.frequency = frequency
        self.left = None
        self.right = None

def BFS( T ):

    dq = deque()

    dq.append((T.left, "0"))
    dq.append((T.right, "1"))

    while len(dq) > 0:

        curr, direction = dq.popleft()

        if curr.value != '':
            print(curr.value, direction)

        if curr.left != None:
            dq.append((curr.left, direction + "0"))
        
        if curr.right != None:
            dq.append((curr.right, direction + "1"))
        

def Huffman( A ):

    pq = PriorityQueue()

    for drzewo in A:
        pq.put((drzewo.frequency, drzewo)) #Drzewo.frequency juz nie bedzie zwracane inczej jakbym dał w krotce pq.put( (a,b) )

    #Biore dwa najmniejsze
    while not pq.empty(): 

        freq, drzewo1 = pq.get()

        if(pq.empty()): #koniec, ostatni element
            return drzewo1

        freq, drzewo2 = pq.get()

        noweDrzewo = Node('', drzewo1.frequency + drzewo2.frequency)
        
        if drzewo1.frequency <= drzewo2.frequency:
            noweDrzewo.left = drzewo1
            noweDrzewo.right = drzewo2
        else:
            noweDrzewo.left = drzewo2
            noweDrzewo.right = drzewo1

        pq.put((noweDrzewo.frequency, noweDrzewo))

A = [ (Node('a', 700)), (Node('b', 200)), (Node('c', 120)), (Node('d', 300)), (Node('e', 10)) ]#para drzewo, czestosc wystepowania

x =  Huffman( A )
BFS( x )

