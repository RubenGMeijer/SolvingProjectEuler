#!/bin/python3

import sys
import math

t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = list(map(int, list(input().strip())))
    
    bigprod=-1
    for x in range(n-k+1):
        cno=math.prod(num[x:x+k])
        if cno > bigprod:
            bigprod = cno
    print(bigprod)
