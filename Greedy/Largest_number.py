def Largest(list):
    list = sorted(list)
    numS =""
    for _ in range(len(list)):
        numS = numS + str(list.pop())
    return int(numS)

list = [1,3,2,5,6,4]
print(Largest(list))

# Returns 654321
