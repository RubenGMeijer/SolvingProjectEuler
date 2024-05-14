# Enter your code here. Read input from STDIN. Print output to STDOUT

def isTriangular(t):
    n = 0.5 * ((1 + 8*t) ** 0.5 - 1)
    n1 = n // 1
    if n1 == n:
        return int(n1)
    return -1

if __name__ == "__main__":
    for x in range(int(input())):
        print(isTriangular(int(input())))
