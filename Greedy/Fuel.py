# Python program for finding the total 
# number of stops for refilling
# n = number of stations
# x  = array of stops including start, all stations, and destination
# L = distance traveled on full tank of gas

def countRefill(x, n, L):
    numRefills = 0 
    currentRefill = 0
   
    while (currentRefill <= n): 
        lastRefill = currentRefill
        while ((currentRefill <=n) and (x[currentRefill+1]- x[lastRefill] <=L)):
            currentRefill += 1
        if currentRefill == lastRefill:
            return "Impossible"
        if currentRefill <= n:
            numRefills += 1
    return numRefills

if __name__ == '__main__':
    n = 3 
    x = [ 0, 3, 6, 7, 9] 
  
    #function call that returns the answer to the problem
    for L in range(10): 
        print(L,countRefill(x,n,L))

# Algorithm efficiency O(n)
