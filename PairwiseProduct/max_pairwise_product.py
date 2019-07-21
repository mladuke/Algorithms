# python3
# O(n^2) time complexity.  Bad for large list of input numbers


def max_pairwise_product(numbers):
    start = time.time()
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                              numbers[first] * numbers[second])
    end = time.time()
    etime = (end-start)
    return (max_product, etime)

def max_pairwise_product_faster(numbers):
    start = time.time()
    max_product = 0
    s_numbers = sorted(numbers, reverse=True)
    max_product = s_numbers[0]*s_numbers[1]
    end = time.time()
    etime =(end-start)
    return (max_product, etime)


if __name__ == '__main__':
    import random
    import time
    a=1
    b=10000000000
    test = True
    while test == True:
        input_numbers = [random.randint(a, b) for _ in range(2000)]
        #print(input_numbers)
        max1,etime1 =(max_pairwise_product(input_numbers))
        max2,etime2 =(max_pairwise_product_faster(input_numbers))
        if max1 == max2:
            print ("OK", max1,etime1,etime2)
        else:
            test = False 