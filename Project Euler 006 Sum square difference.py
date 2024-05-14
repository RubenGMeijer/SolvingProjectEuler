import sys

t = int(input().strip())
nlist=[]
for a0 in range(t):
    nlist.append(int(input().strip()))

mydifference=[1]
mysum_of_squares=[1]
for x in range(2, max(nlist)+1):
    mydifference.append(x+mydifference[x-2])
    mysum_of_squares.append(x**2+mysum_of_squares[x-2])

mydifference=list(map(lambda a: a**2, mydifference))

mydifference=list(map(lambda a, b: a - b, mydifference, mysum_of_squares))

for x in nlist:
    print(mydifference[x-1])
