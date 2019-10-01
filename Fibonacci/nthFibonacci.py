def getNthFib(n):
    # Write your code here.
	fibo_nums = [0,1]
	i=1
	if(n==1 or n==2):
		return fibo_nums[n-1]
	elif(n>2):
		while (True):
			fib = fibo_nums[i-1]+fibo_nums[i]
			fibo_nums.append(fib)
			if(len(fibo_nums)==n):
				break
			else:
				i+= 1
	return fibo_nums[n-1]

for n in range(1,100):
    print(getNthFib(n))