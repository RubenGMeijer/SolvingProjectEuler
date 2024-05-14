# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

def rearrange(word, res, disorderlist):  # takes three lists
    if disorderlist == []:
        return word + res
    
    x = disorderlist.pop(0)
    word.append(res[x])
    res.pop(x)
    return rearrange(word, res, disorderlist)

if __name__ == "__main__":
    faclist = []
    for x in range(12, 0, -1):
        faclist.append(math.factorial(x))
    
    t=int(input())
    for x in range(t):
        n=int(input())-1  # 0-based indexing hehe xd
        
        disorderlist=[0]*12
        counter = 0
        length=len(faclist)
        
        while counter < length:
            if n >= faclist[counter]:
                disorderlist[counter]+= n//faclist[counter]
                n = n % faclist[counter]
            counter+=1
        # print(disorderlist)
        
        word = rearrange([], list('abcdefghijklm'), disorderlist)
        print(''.join(word))