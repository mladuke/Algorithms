#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalX' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def getTotalX(a, b):
    # Write your code here
    minb = min(b)
    maxa = max(a)
    
    facta =[]
    for i in range(maxa, minb+1):
        fact = True
        for j in a:
            if (i%j !=0):
                fact = False
        if fact == True:
            facta.append(i)
    
    factb=[]
    for i in facta:
        fact = True
        for j in b:
            if (j%i !=0):
                fact = False
        if fact == True:
            factb.append(i)
    
    return len(factb)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    arr = list(map(int, input().rstrip().split()))
    brr = list(map(int, input().rstrip().split()))
    total = getTotalX(arr, brr)
    fptr.write(str(total) + '\n')
    fptr.close()

# 2 3
# 2 4
# 16 32 96

# 3