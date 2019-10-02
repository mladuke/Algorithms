

# Time O(n^2) Space O(1)
# Swap adjacent number if they are not in order
def bubbleSort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1] :
                array[j], array[j+1] = array[j+1], array[j]
    return array

import random
A = [random.randint(1, 100) for iter in range(10)]
n = len(A)
print ("Unsorted array",A)
Asorted = bubbleSort(A)
print ("Sorted array",Asorted)