# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":
    answer=0
    for x in range(1, int(input())+1):
        answer+=pow(x,x,10**10)
    print(answer%10**10)
