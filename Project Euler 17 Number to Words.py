numbers={0:"", 1:" One", 2:" Two",3:" Three", 4:" Four",5:" Five",6:" Six",7:" Seven", 8:" Eight",9:" Nine"}

teens={10:" Ten",11:" Eleven",12:" Twelve",13:" Thirteen",14:" Fourteen",15:" Fifteen",16:" Sixteen",17:" Seventeen",18:" Eighteen",19:" Nineteen"}

tens={20:" Twenty",30:" Thirty",40:" Forty",50:" Fifty",60:" Sixty",70:" Seventy",80:" Eighty",90:" Ninety"}

def convert(n):
    if n<10:
        return numbers[n]
    elif n<20:
        return teens[n]
    elif n<100 and n%10==0:
        return tens[n]
    elif n<100:
        return tens[10*(n//10)] + numbers[n%10]
    elif n<1000:
        return numbers[n//100]+" Hundred"+convert(n%100)
    elif n<1000000:
        return convert(n//1000)+ " Thousand"+convert(n%1000)
    elif n<1000000000:
        return convert(n//1000000)+ " Million" + convert(n%1000000)
    else:
        return convert(n//1000000000)+" Billion" + convert(n%1000000000)

t=int(input().strip())
for _ in range(t):
    n=int(input().strip())
    print(convert(n).strip())
