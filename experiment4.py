from good_sorts import quicksort
from good_sorts import mergesort
from good_sorts import heapsort
from experiment1 import test_time
import matplotlib.pyplot as plot

def main():
    list_sizes_s, times_s = test_time(quicksort)
    list_sizes_i, times_i = test_time(mergesort)
    list_sizes_b, times_b = test_time(heapsort)
    plot.plot(list_sizes_s, times_s)
    plot.plot(list_sizes_i, times_i)
    plot.plot(list_sizes_b, times_b)
    plot.legend(["Quick Sort","Merge Sort","Heap Sort"])
    plot.xlabel("List Sizes")
    plot.ylabel("Time (s)")
    plot.show()

if __name__ == "__main__":
    main()