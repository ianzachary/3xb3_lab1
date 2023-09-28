import matplotlib.pyplot as plot
from good_sorts import mergesort
from experiment4 import test_time


def bottom_up_mergesort(L):
    a = len(L)
    width = 1

    while width < a:
        for i in range(0, a, width*2):
            left = i
            mid = min(width + i, a)
            right = min(width*2 + i, a)
            merge(L, left, right, mid)
        width = 2*width
    return L

def merge(L, left, right, mid):
    temp = []                
    j = left
    k = mid

    while j < mid and k < right:
        # check if smallest element in the left or right sublists
        if L[j] < L[k]:
            temp.append(L[j])
            j += 1
        else:
            temp.append(L[k])
            k += 1

    # check for remaining elements 
    while j < mid:
        temp.append(L[j])
        j += 1

    while k < right:
        temp.append(L[k])
        k += 1
    
    # copy back to original list
    for i in range(left, right):
        L[i] = temp[i - left]

list_sizes1, times1 = test_time(mergesort)
list_sizes2, times2 = test_time(bottom_up_mergesort)

plot.plot(list_sizes1, times1)
plot.plot(list_sizes2, times2)
plot.legend(["Recursive Mergesort", "Iterative Mergesort"])
plot.xlabel("List Sizes")
plot.ylabel("Time (s)")
plot.show()
