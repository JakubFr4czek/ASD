import math

def sito(k):

    T = [0 for _ in range(k + 1)] #lacznie z k

    for i in range(2, int(math.sqrt(k + 1)) + 1):

        if T[i] == 0:

            for j in range(i * i, k + 1, i):
                T[j] = 1

    for i in range(2, len(T)):
        if T[i] == 0:
            print(i, end=' ')

sito(2115)

