# Inputs
# L is a list of points on a line
# r is the max width of a segment

# Outputs
# count is the number of segments formed
# R is a list of segments formed

def pointsCoveredSorted(L,r):
    R = []
    i = 0
    n = len(L)
    count = 0
    while i < n:
        count += 1 
        max = L[i]+r
        newRange =(L[i],max)
        R.append(newRange)
        i += 1
        while ((i < n) and L[i] <= max):
            i += 1
    return R, count

L =[3.6,3.8,4.2,4.6,5,5.5,6,7,8]
r  = 1
R , count = pointsCoveredSorted(L,r)
print("Input List: ",L)
print("Range allowed in a group: ", r)
print("Number of Groups formed: ", count)
print("List of Groups: ", R)
print()
L =[3.6,3.8,4.2,4.6,5,5.5,6,7,8]
r  = 5
R , count = pointsCoveredSorted(L,r)
print("Input List: ",L)
print("Range allowed in a group: ", r)
print("Number of Groups formed: ", count)
print("List of Groups: ", R)

# Input List:  [3.6, 3.8, 4.2, 4.6, 5, 5.5, 6, 7, 8]
# Range allowed in a group:  1
# Number of Groups formed:  3
# List of Groups:  [(3.6, 4.6), (5, 6), (7, 8)]
#
# Input List:  [3.6, 3.8, 4.2, 4.6, 5, 5.5, 6, 7, 8]
# Range allowed in a group:  5
# Number of Groups formed:  1
# List of Groups:  [(3.6, 8.6)]