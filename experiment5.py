from good_sorts import quicksort
from experiment3 import test_near_sorted_list
import matplotlib.pyplot as plot

def main():
    list_sizes_s, times_s = test_near_sorted_list(quicksort, n=995)
    plot.plot(list_sizes_s, times_s)
    plot.legend(["Quick Sort"])
    plot.xlabel("Swaps")
    plot.ylabel("Time (s)")
    plot.show()

if __name__ == "__main__":
    main()