def poly_mult_naive(A,B):
    alen = len(A)
    blen = len(B)
    if (alen != blen):
        print ("Input array must be the same size")
        return -1
    product =[0] * (2*alen - 1)
    for i in range(len(A)):
        for j in range(len(B)):
            product[i+j] = product[i+j] +A[i]*B[j]
    return product
A=[4,7,2,5]
B=[1,3,9,2]

print(poly_mult_naive(A,B))