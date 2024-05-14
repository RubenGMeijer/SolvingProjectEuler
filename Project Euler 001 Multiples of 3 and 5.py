import sys
import math

def ceildiv(a, b):
    return -(a // -b)

def sum_numbers(n, d):
    #n = number up to which sum of all multiples of d are found
    return (n-1)//d * ceildiv(n, d) * d // 2

t = int(input().strip())
for x in range(t):
    n = int(input().strip())
    print(sum_numbers(n, 3)+sum_numbers(n, 5)-sum_numbers(n, 15))