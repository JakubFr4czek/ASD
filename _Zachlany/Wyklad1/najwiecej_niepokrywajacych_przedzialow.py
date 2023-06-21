from queue import PriorityQueue
from collections import deque

#Zachlan, biore te ktore koncza sie najwczesniej

def nnp( A ):

    dq = deque()
    pq = PriorityQueue()

    for poczatek, koniec in A:
        pq.put((koniec, poczatek)) #bo najpierw te ktore koncza sie najwczesniej

    c_koniec, c_poczatek = pq.get()
    dq.append( (c_poczatek, c_koniec) )

    while not pq.empty():

        n_koniec, n_poczatek = pq.get() #n od next

        if n_poczatek >= c_koniec:
            c_poczatek = n_poczatek
            c_koniec = n_koniec
            dq.append( (c_poczatek, c_koniec) )
                
    return dq


A = [ (0,2), (1,4), (3,6), (5, 8), (8,9) ]

print(nnp(A))
