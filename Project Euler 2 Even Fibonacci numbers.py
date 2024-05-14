import math

def get_fibonacci(n):
    return round((((1+5**0.5)/2)**n-(1-(1+5**0.5)/2)**n)/(5**0.5))  # computer rounding hehe

def get_index_fibonacci(f):  # returns floor
    return math.floor(math.log(f*5**0.5, (1+5**0.5)/2))

fibonaccilist=[0, 1]
for x in range(2, 82):
    fibonaccilist.append(fibonaccilist[x-2]+fibonaccilist[x-1])

t = int(input().strip())
for a0 in range(t):
    f = int(input().strip())
    n = get_index_fibonacci(f)
    counter2=0
    for x in range(3, n+1, 3):
        counter2+=fibonaccilist[x]
    print(counter2)
