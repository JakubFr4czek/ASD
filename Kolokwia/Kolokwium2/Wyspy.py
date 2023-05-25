from queue import PriorityQueue

def print_arr(A):

    for i in range(len(A)):
        print(A[i])

def Dijkstra(G, v, t):

    path = [-1] * len(G)
    distance = [float('inf')] * len(G)
    queue = PriorityQueue()

    distance[v] = 0
    queue.put((0, v))

    while not queue.empty() > 0:

        priority, temp = queue.get()

        for i in range(len(G[temp])):

            if G[temp][i] != 0 and priority != G[temp][i]:
                if distance[i] > priority + G[temp][i]:
                    distance[i] = priority + G[temp][i]
                    path[i] = temp
                    queue.put((distance[i], i))
    
    print(distance[t])


G = [[0,5,1,8,0,0,0],
     [5,0,0,1,0,8,0],
     [1,0,0,8,0,0,8],
     [8,1,8,0,5,0,1],
     [0,0,0,5,0,1,0],
     [0,8,0,0,1,0,5],
     [0,0,8,1,0,5,0]]

Dijkstra(G, 5, 0)