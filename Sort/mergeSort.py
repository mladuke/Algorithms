def merge(array, left, middle, right):
    left_array_size = int(middle - left + 1)
    right_array_size = int(right - middle)
    left_array = [0] * (left_array_size)
    right_array = [0] * (right_array_size)
    for left_array_p in range(0, left_array_size):
        left_array[left_array_p] = array[left + left_array_p]
    for right_array_p in range(0, right_array_size):
        right_array[right_array_p] = array[middle + 1 + right_array_p]
    left_array_p = 0
    right_array_p = 0
    sorted_array_p = left
    while  left_array_p < left_array_size and right_array_p < right_array_size:
        if left_array[left_array_p] <= right_array[right_array_p]:
            array[sorted_array_p] = left_array[left_array_p]
            left_array_p += 1
        else:
            array[sorted_array_p] = right_array[right_array_p]
            right_array_p += 1
        sorted_array_p += 1    
    while left_array_p < left_array_size: 
	    array[sorted_array_p] = left_array[left_array_p] 
	    left_array_p += 1
	    sorted_array_p += 1
    while right_array_p < right_array_size: 
	    array[sorted_array_p] = right_array[right_array_p] 
	    right_array_p += 1
	    sorted_array_p += 1

def mergeSort(array,left,right): 
	if left < right: 
		middle = int((left+(right-1))/2)
		mergeSort(array, left, middle) 
		mergeSort(array, middle+1, right) 
		merge(array, left, middle, right) 

import random
array = [random.randint(1, 100) for iter in range(10)]
n = len(array) 
print ("Given array is", array) 
mergeSort(array,0,n-1) 
print ("\n\nSorted array is", array)