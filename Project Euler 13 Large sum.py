n=int(input())

bigno=0
for x in range(n):
    bigno+=int(input()[:14])

print(str(bigno)[:10])
