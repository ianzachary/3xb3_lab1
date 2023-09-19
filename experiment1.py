import timeit
import random
import matplotlib.pyplot as plot
from bad_sorts import create_random_list
from bad_sorts import insertion_sort
from bad_sorts import selection_sort

def test_insertion(n, m, step):
    times = []
    list_sizes = []
    for i in range(0, n, step):
        time = 0
        for _ in range(m):
            L = create_random_list(i, i)
            start = timeit.default_timer()
            L2 = selection_sort(L)
            end = timeit.default_timer()
            time += end - start
        times.append(time/m)
        list_sizes.append(i)
    return list_sizes, times

list_sizes, times = test_insertion(1000, 10, 50)
plot.plot(list_sizes, times)
plot.xlabel("List Sizes")
plot.ylabel("Time (s)")
plot.show()
#print(time)