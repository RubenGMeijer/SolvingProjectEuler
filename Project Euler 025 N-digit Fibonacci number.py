# Enter your code here. Read input from STDIN. Print output to STDOUT

import math
import sys

def fibonaccidigits(n):
    flist = [0, 1]
    for x in range(2, n):
        flist.append(flist[x-2]+flist[x-1])
    for x in range(n):
        flist[x] = len(str(flist[x]))
    return flist
    
if __name__ == "__main__":
    
    sys.set_int_max_str_digits(10000)
    
    phi = (1+5**0.5)/2
    
    t=int(input())
    nlist=[]
    for x in range(t):
        nlist.append(int(input()))

    nmax=max(nlist)
    
    flist = [0, 1]
    lenlist= [1, 1]
    
    counter=1
    while lenlist[counter] < nmax:
        counter+=1
        flist.append(flist[0]+flist[1])
        lenlist.append(len(str(flist[2])))
        flist.pop(0)
    
    for x in nlist:
        print(lenlist.index(x))
