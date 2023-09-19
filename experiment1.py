import timeit
import matplotlib.pyplot as plot
from bad_sorts import create_random_list
from bad_sorts import insertion_sort
from bad_sorts import selection_sort
from bad_sorts import bubble_sort


def test_time(n, m, step, function):
    times = []
    list_sizes = []
    for i in range(0, n, step):
        time = 0
        for _ in range(m):
            L = create_random_list(i, i)
            start = timeit.default_timer()
            L2 = function(L)
            end = timeit.default_timer()
            time += end - start
        times.append(time/m)
        list_sizes.append(i)
    return list_sizes, times

list_sizes_s, times_s = test_time(1000, 10, 50, selection_sort)
list_sizes_i, times_i = test_time(1000, 10, 50, insertion_sort)
list_sizes_b, times_b = test_time(1000, 10, 50, bubble_sort)
plot.plot(list_sizes_s, times_s)
plot.plot(list_sizes_i, times_i)
plot.plot(list_sizes_b, times_b)
plot.legend(["Selection Sort","Insertion Sort","Bubble Sort"])
plot.xlabel("List Sizes")
plot.ylabel("Time (s)")
plot.show()
#print(time)