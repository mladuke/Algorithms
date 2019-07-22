# Python program to display the Fibonacci sequence up to n-th term using recursive functions


def recur_fibo(n):
    """Recursive function to
    print Fibonacci sequence"""
    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))


def fibo_fast(n):
    """Fast function to
    print Fibonacci sequence"""
    fib = {}
    fib[0] = 0
    fib[1] = 1
    for i in range(2,n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]


# Change this value for a different result
nterms = 20

# uncomment to take input from the user
#nterms = int(input("How many terms? "))

# check if the number of terms is valid
if nterms <= 0:
    print("Plese enter a positive integer")
else:
    print("Index Fibonacci sequence:")
    for i in range(nterms):
        print(i,recur_fibo(i), fibo_fast(i))
    for i in range(nterms+1,1000):
        print(i,fibo_fast(i))

# Running Time recur_fibo
# T(n) = 2 if n <= 1
# T(n) = 3 + T(n-1) +T(n-2) for n >= 2
# T(n) >= F(n)
# T(100) approx 1.77 * 10^21 lines of code executed

# Running Time fibo_fast
# T(n) = 2n+2
# T(100) = 202 lines of code