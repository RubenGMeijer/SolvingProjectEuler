import sys
import math

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    sqrt2=2**0.5
    
    # x=math.ceil(0.25*n)
    y=math.ceil(0.5*n)-1
    z=math.floor(n/(2+sqrt2))
    
    largest3=-1
    
    j=1
    i=y
    while i > z:
        k=n-i-j
        k2=k**2
        ij2=i**2+j**2
        if k2 == ij2:
            if i*j*k > largest3:
                largest3=i*j*k
            i+=-1
        elif k2 > ij2:
            j+=1
        else:
            i+=-1
            
    print(largest3)
