''' # Copyright © 2019 AlgoExpert, LLC. All rights reserved.
# O(n) time | O(1) space

def findThreeLargestNumbers(array):
    threeLargest = [None, None, None]
    for num in array:
        print(num)
        updateLargest(threeLargest, num)
    print(threeLargest)
    print("_______________")
    return threeLargest

def updateLargest(threeLargest, num):
    if threeLargest[2] is None or num > threeLargest[2]:
        shiftAndUpdate(threeLargest, num, 2)
    elif threeLargest[1] is None or num > threeLargest[1]:
        shiftAndUpdate(threeLargest, num, 1)
    elif threeLargest[0] is None or num > threeLargest[0]:
        shiftAndUpdate(threeLargest, num, 0)

def shiftAndUpdate(array, num, idx):
    for i in range(idx + 1):
        if i == idx:
            array[i] = num
        else:
            array[i] = array[i + 1] '''

# Input: Array of Integers i.e [10,5,9,10,12]
# Output Sorted array of 3 largest integers, including duplicates i.e [10,10,12]

def findThreeLargestNumbers(array):
    # Write your code here.
    array1 = sorted(array, reverse=True)
    return sorted(array1[0:3])

