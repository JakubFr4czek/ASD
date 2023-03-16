from bubblesort import bubblesort
from selectionsort import selectionsort
from insertionsort import insertionsort
from mergesort import mergesort
from heapsort import heapsort
from quicksort import quicksort

tab = [1,2,3,5,3,2,1,5,7,7,4,3,2,3,4]

#bubblesort(tab)
#selectionsort(tab)
#insertionsort(tab)
quicksort(tab, 0, len(tab) - 1)
#mergesort(tab, 0, len(tab) - 1)
#heapsort(tab)


print(tab)

