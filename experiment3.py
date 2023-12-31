import timeit
import matplotlib.pyplot as plot
from bad_sorts import create_near_sorted_list
from bad_sorts import selection_sort
from bad_sorts import bubble_sort
from bad_sorts import insertion_sort


def test_near_sorted_list(function, n = 1000, m = 100, swaps = 50):
    times, s = [], []
    for i in range(0, n, swaps):
        time = 0
        for _ in range(m):
            L = create_near_sorted_list(n, n, i)
            start = timeit.default_timer()
            L2 = function(L)
            end = timeit.default_timer()
            time += end - start
        times.append(time/m)
        s.append(i)
    return s, times

def main():
    swaps_s, times_s = test_near_sorted_list(selection_sort)
    swaps_i, times_i = test_near_sorted_list(insertion_sort)
    swaps_b, times_b = test_near_sorted_list(bubble_sort)
    plot.plot(swaps_s, times_s)
    plot.plot(swaps_i, times_i)
    plot.plot(swaps_b, times_b)
    plot.legend(["Selection Sort","Insertion Sort","Bubble Sort"])
    plot.xlabel("Swaps")
    plot.ylabel("Time (s)")
    plot.show()

if __name__ == "__main__":
    main()