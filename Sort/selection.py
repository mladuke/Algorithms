import random


def selection_sort(X):
    A = X.copy()
    for i in range(len(A)):
        min_index = i
        for j in range(i+1, len(A)):
            if A[min_index] > A[j]:
                min_index = j
        A[i], A[min_index] = A[min_index], A[i]
    return A

def selectionSort(array):
    # Write your code here.
    aLength = len(array)
    for i in range(0, aLength-1):
        jMin = i
        for j in range(i+1, aLength):
            if (array[j] < array[jMin]):
                jMin = j
        if (jMin != i):
            temp = array[jMin]
            array[jMin] = array[i]
            array[i] = temp
    return array

A = [random.randint(1, 100) for iter in range(10)]
Asorted = selection_sort(A)
print ("Unsorted array", A)
print("Sorted array", Asorted)

print ("Unsorted array", A)
Asorted = selectionSort(A)
print ("Sorted array", Asorted)