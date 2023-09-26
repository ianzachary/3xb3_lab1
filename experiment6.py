from good_sorts import quicksort
from experiment1 import test_time
import matplotlib.pyplot as plot


def dual_quicksort_copy(L):
    if len(L) < 3:
        return sorted(L)
    if L[0] > L[1]:
        pivot1, pivot2 = L[1], L[0]
    else:
        pivot1,pivot2 = L[0], L[1]
    left, middle, right = [], [], []
    for num in L[2:]:
        if num < pivot1:
            left.append(num)
        elif num > pivot2:
            right.append(num)
        else:
            middle.append(num)
    #print(dual_quicksort_copy(left), [pivot1], middle, dual_quicksort_copy(middle), [pivot2], dual_quicksort_copy(right))
    return dual_quicksort_copy(left) + [pivot1] + dual_quicksort_copy(middle) + [pivot2] + dual_quicksort_copy(right)

def dual_quicksort(L):
    copy = dual_quicksort_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]
    return L

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