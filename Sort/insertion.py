def insertionSort(array):
    # Write your code here.
	index = 1
	while (index < len(array)):
		j = index
		while ( (j>0) and (array[j-1]>array[j] ) ):
			temp = array[j-1]
			array[j-1] = array[j]
			array[j] = temp
			j -= 1
		print(array)
		index += 1
	return array	

import random
array = [random.randint(1, 100) for iter in range(10)]
n = len(array) 
print ("Given array is", array) 
insertionSort(array) 
print ("\n\nSorted array is", array)