from collections import deque
#Zlozonosc O(ElogV)
#Trzeba uzyc kolejki priorytetowej -> minHeap


#v - wierzcholek startowy
def Prim(G, v):

    distance = [float('inf') for _ in range(len(G))]
    parent = [-1 for _ in range(len(G))]





G = [

    [(1,1), (4,4), (5, 8)],
    [(0,1), (2,3)],
    [(1,3), (4,4), (3,6)],
    [(2,6), (4,2)],
    [(0,4), (2,4), (3,2), (5,7)],
    [(0,8), (4,7)]

]

Prim(G, 0)

