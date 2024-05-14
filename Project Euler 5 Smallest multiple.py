#!/bin/python3

import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    counter=1
    
    found=False
    while not found:
        for x in range(n, n//2, -1):
            if counter % x != 0:
                counter+=1
                break
        else:
            found=True
        
    print(counter)
