## Dot product of two vectors of n dimensions:

## Input as a list

# n--> number of dimensions in a vector
# a,b are two vectors of n dimensions, in list format and n is an integer

def dot_pro(n,a,b):
    c=0
    for i in range(0,n):
        c=a[i]+b[i]
    return c
