from good_sorts import quicksort
from good_sorts import mergesort
from good_sorts import heapsort
from experiment3 import test_near_sorted_list
import matplotlib.pyplot as plot

def main():
    list_sizes_s, times_s = test_near_sorted_list(quicksort, n = 950)
    list_sizes_m, times_m = test_near_sorted_list(mergesort, n = 950)
    list_sizes_h, times_h = test_near_sorted_list(heapsort, n = 950)

    plot.plot(list_sizes_s, times_s)
    plot.plot(list_sizes_m, times_m)
    plot.plot(list_sizes_h, times_h)

    plot.legend(["Quick Sort", "Merge Sort", "Heap Sort"])
    plot.xlabel("Swaps")
    plot.ylabel("Time (s)")
    plot.show()

if __name__ == "__main__":
    main()