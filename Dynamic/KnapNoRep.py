def zeroOneKnapsack(v, w, W):
    c = []
    n = len(v)
    c = [[0 for x in range(W+1)] for x in range(n)]  
    for i in range(0,n):
        for j in range(0,W+1):		
            if (w[i] > j):
                c[i][j] = c[i-1][j]
            else:
                c[i][j] = max(c[i-1][j],v[i] +c[i-1][j-w[i]])
    return [c[n-1][W], getUsedItems(w,c)]

def getUsedItems(w,c):
	i = len(c)-1
	currentW =  len(c[0])-1
	marked = []
	for i in range(i+1):
		marked.append(0)			
	while (i >= 0 and currentW >=0):
		if (i==0 and c[i][currentW] >0 )or c[i][currentW] != c[i-1][currentW]:
			marked[i] =1
			currentW = currentW-w[i]
		i = i-1
	return marked

# adapted from  https://sites.google.com/site/mikescoderama/Home/0-1-knapsack-problem-in-p

W = 10
v = [9, 14, 16, 30]
w = [2, 3, 4, 6]

print(zeroOneKnapsack(v, w, W))
    