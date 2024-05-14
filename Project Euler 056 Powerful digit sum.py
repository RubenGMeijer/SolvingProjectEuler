
def digitSum(n):
    return sum(map(int, str(n)))

if __name__ == "__main__":
    n=int(input())
    maxSum=0
    for x in range(n):
        for y in range(n):
            curSum=digitSum(x**y)
            if curSum > maxSum:
                maxSum = curSum
    print(maxSum)
