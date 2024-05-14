import sys

t = int(input().strip())
for x in range(t):
    n = int(input().strip())
    palindrome=0
    for x in range(n-1, 101100, -1):
        if str(x)==str(x)[::-1] and any([x% y == 0 and len(str(x//y)) == 3 for y in range(999, 99, -1)]):
            palindrome=x
            break
    print(palindrome)
