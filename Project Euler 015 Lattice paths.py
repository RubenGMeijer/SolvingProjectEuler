import math

n=int(input())

for x in range(n):
    a, b = map(int, input().split())
    print((math.factorial(a+b)//math.factorial(a)//math.factorial(b)) % (10**9+7))
