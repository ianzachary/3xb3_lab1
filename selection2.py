import matplotlib.pyplot as plot
from bad_sorts import selection_sort, swap 
from experiment1 import test_time

def selection_sort2(L):
    i = 0
    k = len(L) - 1
    while i < k:
        min_index, max_index = findMaxMin_index(L, i, k)
        if i == max_index:
            max_index = min_index
        elif k == i:
            k = min_index
        swap(L, i, min_index)
        swap(L, k, max_index)
        i += 1
        k -= 1
    return L

def findMaxMin_index(L, n, k):
    min_index = n
    max_index = n
    for i in range(n+1, k+1):
        if L[i] < L[min_index]:
            min_index = i
        elif L[i] > L[max_index]:
            max_index = i
    return min_index, max_index

list_sizes1, times1 = test_time(selection_sort)
list_sizes2, times2 = test_time(selection_sort2)

plot.plot(list_sizes1, times1)
plot.plot(list_sizes2, times2)
plot.legend(["Selection 1", "Selection 2"])
plot.xlabel("List Sizes")
plot.ylabel("Time (s)")
plot.show()
