def GCD_Slow(a,b):
    best = 0
    for d in range(1,a+b+1):
        print(d, best)
        if (a%d ==0  and b%d==0):
            best = d
            print(d)
    return best

def GCD_Fast(a,b):
    ''' Euclidean Algorithm
    '''
    print (a,b)
    if (b == 0):
        return a
    aprime = a%b
    return(GCD_Fast(b,aprime))

a=357
b=234

print (GCD_Fast(a,b))
print(GCD_Slow(a,b))

# Efficiency
# GCD_Slow is O(a+b)
# GCD_Fast is O(log(a*b))
