def russian(a,b):
    x = a; y = b
    z = 0
    while x > 0:
        if (x % 2 == 1):
            z = z + y
        y = y << 1
        x = x >> 1
    return z

print(russian(10,6))

def rec_russian(a,b):
    if a==0:
        return 0
    if a%2 == 0:
        return 2*rec_russian(a/2,b)
    return b + 2*rec_russian((a-1)/2,b)

print(rec_russian(10,6))


