def multiply1(x,y):
    n = len(x)
    if (n==1):
        return x[0]*y[0]
    s = int(n/2)
    xl = x[0:s]
    xh = x[s:]
    yl = y[0:s]
    yh = y[s:]
    p1 = multiply(xl,yl)
    p2 = multiply(xh,yh)
    xz = [x1 + x2 for x1, x2 in zip(xl, xh)]
    yz = [y1 + y2 for y1, y2 in zip(yl, yh)]
    p3 = multiply(xz,yz)
    if isinstance(p2, list):
        t2 = [p3t -p2t - p1t for p1t, p2t, p3t in zip(p1,p2,p3 )]
    else:
        t2 = p3-p2-p1  
    return [p1,t2,p2]

def multiply(X,Y):
    if ((len(X)==1) or (len(X)==2)):
        return (multiply1(X,Y))
    elif (len(X)==4):
        p1,p2,p3 = multiply1(X,Y)
        return ([p1[0],p1[1],(p1[2]+p2[0]),p2[1],(p2[2]+p3[0]),p3[1],p3[2]])
    else:
        print("polnomial order must be 1, 2, or 4")
        return -1

x=[4,7,2,5]
y=[1,3,9,2]

print(multiply(x,y))
