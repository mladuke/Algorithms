# Enter your code here. Read input from STDIN. Print output to STDOUT
# input: number of operations, and deque of operations
# output : space sepeated elements of deque d
from collections import deque
d=deque()
n = int(input())
for i in range(n):
    c= input().split()
    if c[0]=="append":
        d.append(int(c[1]))
    elif c[0]=="appendleft":
        d.appendleft(int(c[1]))
    elif c[0]=="pop":
        d.pop()
    elif c[0]=="popleft":
        d.popleft()
print(* d)