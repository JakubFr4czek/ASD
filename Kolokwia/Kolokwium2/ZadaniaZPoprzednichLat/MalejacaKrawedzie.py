from collections import deque


def MalejaceKrawedzie(G, v, t):

    queue = deque()

    queue.append((0, float('inf')))

    while len(queue) > 0:
        
        temp, val = queue.pop()

        if temp == t:
            print("Hoooj", temp, val)
            return

        for i in range(len(G[temp])):

            if G[temp][i][1] < val:
                queue.append((G[temp][i][0], G[temp][i][1]))


G = [

    [(3,10)],
    [(4,7)],
    [(1,8), (6,10), (5,5)],
    [(2,9)],
    [(2,6)],
    [(2,3)],
    [(5,7)]

]

MalejaceKrawedzie(G, 0, 5)