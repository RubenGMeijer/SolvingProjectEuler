import math

if __name__ == "__main__":
    t=int(input())
    
    for x in range(t):
        n=str(math.factorial(int(input())))
        counter=0
        for y in n:
            counter+=int(y)
        print(counter)