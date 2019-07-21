# Python program to display the Fibonacci sequence up to n-th term using recursive functions

def recur_fibo(n):
   """Recursive function to
   print Fibonacci sequence"""
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

# Change this value for a different result
nterms = 40

# uncomment to take input from the user
#nterms = int(input("How many terms? "))

# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Index Fibonacci sequence:")
   for i in range(nterms):
       print(i, recur_fibo(i))

# Running Time
# T(n) = 2 if n <= 1
# T(n) = 3 + T(n-1) +T(n-2) for n >= 2
# T(n) >= F(n)
# T(100) approx 1.77 * 10^21 lines of code executed