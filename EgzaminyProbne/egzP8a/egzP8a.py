from egzP8atesty import runtests 

#Ogólnie sortuje po pierwszej wspolrzednej
#Teraz dla kazdej firmy szukam bin searchem przedzial po prawej
#Wczesniej kazdy przedzial zawiera informacje o najwiekszej wartosci na prawo od niego

def binary_search(tab, i, j, key):

    if i > j: return i

    mid = (i + j) // 2

    if key < tab[mid][0][0]:
        return binary_search(tab,i, mid - 1, key)
    elif key > tab[mid][0][0]:
        return binary_search(tab, mid + 1, j, key)
    else:
        return mid
    

def reklamy ( T, S, o ):

    dp = [-1] * len(S) #Maks hajsu z obecnego przedzialu lub kazdego na prawo

    A = []

    for i in range(len(T)):
        A.append((T[i], S[i])) #sortuje po pierwszej wspolrzednej

    A.sort() #O(nlogn)
    #dla jedej firmy:

    #Licze ile jest maks kasy do zdobycia dla przedzialu, albo dla kazdego na prawo od niego
    dp[len(A) - 1] = A[len(A) - 1][1]

    for i in range(len(A) - 2, -1, -1): #O(n)

        dp[i] = max(dp[i + 1], A[i][1])

    #Teraz dla kazdego przedzialu szukam bin_searchem kolejny ktory na niego nie nachodzi i w dp
    #Mam max wartosc kazdego kolejnego ktory na niego nie nachodzi

    maxi = -1

    for i in range(len(A)): #O(nlogn)

        idx = binary_search(A, i + 1, len(A) - 1, A[i][0][1] + 1)
        
        if A[i][1] > maxi:
            maxi = A[i][1]

        if idx < len(A) and A[i][1] + dp[idx] > maxi:
            maxi = A[i][1] + dp[idx]

    return maxi

T = [ (0, 3), (4, 5), (1, 4) ]
S = [ 5000, 3000, 15000 ]

#print(reklamy(T,S, 5))

runtests ( reklamy, all_tests=True ) #To wszystko na niby