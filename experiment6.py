from good_sorts import quicksort
from experiment1 import test_time
import matplotlib.pyplot as plot


def dual_quicksort_copy(L):
    if len(L) < 3:
        return L
    if L[0] > L[1]:
        pivot1, pivot2 = L[1], L[0]
    else:
        pivot1,pivot2 = L[0], L[1]
    left, midle, right = [], [], []
    for num in L[2:]:
        if num < pivot1:
            left.append(num)
        elif num > pivot2:
            right.append(num)
        else:
            midle.append(num)
    return dual_quicksort_copy(left) + [pivot1, pivot2] + dual_quicksort_copy(right)

def dual_quicksort(L):
    copy = dual_quicksort(L)
    for i in range(len(L)):
        L[i] = copy[i]

def main():
    list_sizes_s, times_s = test_time(quicksort)
    list_sizes_d, times_d = test_time(dual_quicksort)
    plot.plot(list_sizes_s, times_s)
    plot.plot(list_sizes_d, times_d)
    plot.legend(["Quick Sort", "Dual Quick Sort"])
    plot.xlabel("List Sizes")
    plot.ylabel("Time (s)")
    plot.show()

if __name__ == "__main__":
    main()