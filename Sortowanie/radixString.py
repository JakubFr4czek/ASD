def radix(T, pos, tPos):

    buckets = [ [] for _ in range(26) ] #od a do z

    for i in range(len(T)):
        if pos < len(T[i]):
            buckets[ord(T[i][pos]) - 97].append(T[i])
        else:
            T[tPos] = T[i]
            tPos+=1

    for i in range(len(buckets)):

        if len(buckets[i]) > 1:
            radix(buckets[i], pos + 1, 0)

        for j in range(len(buckets[i])):

            T[tPos] = buckets[i][j]
            tPos+=1
    


T = ["abcd", "abc", "bca", "afg", "amg", "lsd", "yeti", "agb", "ybybybyby", "lcd"]


radix(T, 0, 0)
print(T)


X = ["abcd", "abc", "bca", "afg", "amg", "lsd", "yeti", "agb", "ybybybyby", "lcd"]

X.sort()

print(X)




