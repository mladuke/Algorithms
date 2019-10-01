def factorial(n):
    #base case
    if n==0:
         return 1
    # recursive
    return n*factorial(n-1)

print("i","factorial")
for i in range(10):
    print(i, factorial(i))
