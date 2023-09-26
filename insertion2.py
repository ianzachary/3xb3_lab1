import matplotlib.pyplot as plot
from bad_sorts import insertion_sort
from experiment1 import test_time

def insertion_sort2(L):
    for i in range(1, len(L)):
        insert2(L, i)
    return L


def insert2(L, i):
    value = L[i]
    while i > 0 and L[i - 1] >= value:
        L[i] = L[i - 1]
        i -= 1
    L[i] = value
    return L
        
list_sizes1, times1 = test_time(insertion_sort)
list_sizes2, times2 = test_time(insertion_sort2)

plot.plot(list_sizes1, times1)
plot.plot(list_sizes2, times2)
plot.legend(["Insertion 1", "Insertion 2"])
plot.xlabel("List Sizes")
plot.ylabel("Time (s)")
plot.show()