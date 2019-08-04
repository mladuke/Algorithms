def selection_sort(X):
    A = X.copy()  
    for i in range(len(A)): 
        min_index = i 
        for j in range(i+1, len(A)): 
            if A[min_index] > A[j]:   
                min_index = j                  
        A[i], A[min_index] = A[min_index], A[i]
    return A 
  
import random

A = [random.randint(1, 100) for iter in range(10)]
Asorted = selection_sort(A)
print ("Unsorted array",A) 
print ("Sorted array",Asorted) 