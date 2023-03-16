def partition(tab, l, r): #zalozylismy ze funkcjie partition juz mamy

    pivot = r

    greater = l

    for i in range(l, pivot):

        if tab[i] <= tab[pivot]:
            tab[i], tab[greater] = tab[greater], tab[i] 
            greater+=1

    tab[greater], tab[pivot] = tab[pivot], tab[greater]  
            
    return pivot


#mozemy uzywac appenda (profesor Faliszewski praised)
# nie dziala (:
def quicksort(tab, l, r):

    stack = [(l, r)]

    while len(stack) > 0: #while stos != []

        arg = stack.pop()

        pivot = partition(tab, arg[0], arg[1])

        if arg[0] < pivot - 1:
            stack.append((arg[0], pivot - 1))

        if pivot + 1 < arg[1]:
            stack.append(pivot + 1, arg[1])


tab = [2,5,6,4,3,5,6,4,3,4,5,8,9,7,5,4]
quicksort(tab, 0, len(tab) - 1)
print(tab)
