
if __name__ == "__main__":
    n=int(input())
    
    solDict = {}
    for x in range(1, n+1):
        xLych=x
        for y in range(60):
            xLychRev=int(str(xLych)[::-1])
            if xLych == xLychRev:
                if xLych in solDict.keys():
                    solDict[xLych]+=1
                else:
                    solDict[xLych]=1
                break
            xLych+=xLychRev
    
    maxConvPal = max(solDict, key=lambda x: solDict[x])
    print(maxConvPal, solDict[maxConvPal])
            
