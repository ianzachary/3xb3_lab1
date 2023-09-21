import timeit
import matplotlib.pyplot as plot
from bad_sorts import create_random_list
from bad_sorts import bubble_sort
from experiment1 import test_time

# Traditional Bubble sort
def bubble_sort2(L):
    #for i in range(len(L)):
        for j in range(len(L) - 1):
            if L[j] > L[j+1]:
                # save j+1 element
                element = L[j+1]
                # write values greater than j+1 to 1 above 
                # their current index
                for k in range(j, -1, -1):
                    
                    if (L[k] > element):
                        L[k+1] = L[k]
                        if (k == 0): 
                            L[k] = element
                            break
                    else:  
                        L[k+1] = element
                        break

list_sizes_b, times_b = test_time(bubble_sort)
list_sizes_b2, times_b2 = test_time(bubble_sort2)

plot.plot(list_sizes_b, times_b)
plot.plot(list_sizes_b2, times_b2)
plot.legend(["Bubble 1", "Bubble 2"])
plot.xlabel("List Sizes")
plot.ylabel("Time (s)")
plot.show()