#Tkanina o wymiarze XxY
#T - skrawki o poli xi * yi o wartosci Ci
#Zmaksymalizowac zyks

# a * b - dostepny obszar
# x * y - do wyciecia
def ciecie(T, C, a, b, x):

    res = 0
    c1 = 0
    c2 = 0
    c3 = 0

    return res



def tkanina(T, C, x, y):

    maxi = float('-inf')
    for i in range(len(T)):
        maxi = max(maxi, ciecie(T, C, x, y))
        print(maxi)

x = 10
y  = 10

T = [(1,4), (2,3), (5,5), (9,9), (10,10), (3,4)]
C = [3,4,3,1,7,6]

tkanina(T, C, x, y)