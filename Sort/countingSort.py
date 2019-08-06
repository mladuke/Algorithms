def counting_sort(array, max_val):
    values = max_val + 1
    size = len(array)
    count = [0] * values
    array1 = [0] * size
    
    for num in array:
        count[num] += 1             
    index = 0
    for value in range(values):         
        for _ in range(count[value]):  
            array1[index] = value
            index += 1
    return array1


import random
array = [random.randint(0, 3) for iter in range(20)]
print("Unsorted",array)
print("Sorted",counting_sort(array, 3 ))