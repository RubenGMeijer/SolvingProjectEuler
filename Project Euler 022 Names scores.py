# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == "__main__":
    n = int(input())
    namelist=[]
    for x in range(n):
        namelist.append(input())
    namelist.sort()
    
    q = int(input())
    
    for x in range(q):
        name=input()
        score = namelist.index(name)+1
        score2 = 0
        for y in name:
            score2 += (ord(y)-64)    
        print(score*score2)