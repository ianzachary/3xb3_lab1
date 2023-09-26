from good_sorts import *
from bad_sorts import *
from experiment1 import test_time
import matplotlib.pyplot as plot


def main():
    list_lengths_i, times_i = test_time(insertion_sort, 30, 1000, 1)
    list_lengths_m, times_m = test_time(mergesort, 30, 1000, 1)
    list_lengths_q, times_q = test_time(quicksort, 30, 1000, 1)
    plot.plot(list_lengths_i, times_i)
    plot.plot(list_lengths_m, times_m)
    plot.plot(list_lengths_q, times_q)
    plot.legend(["Insertion Sort", "Mergesort", "Quicksort"])
    plot.xlabel("List Lengths")
    plot.ylabel("Time (s)")
    plot.show()


if __name__ == "__main__":
    main()