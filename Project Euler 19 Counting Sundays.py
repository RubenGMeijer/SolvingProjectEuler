import datetime

def monthAdvance(date):
    date[1] +=1
    if date[1]>12:
        date[1]=1
        date[0]+=1
        #print(date[0], date2[0])
    return date

def firstSundays(date1, date2):  # date: [year, month, day]
    
    if date1[2] > 1:
        monthAdvance(date1)
        date1[2]=1
    date2[2]=1
    
    counter=0
    
    while date1[0] < date2[0]:
        if datetime.date(date1[0], date1[1], 1).weekday() == 6:
            counter+=1
        date1 = monthAdvance(date1)
    while date1[1] < date2[1]:
        if datetime.date(date1[0], date1[1], 1).weekday() == 6:
            counter+=1
        date1 = monthAdvance(date1)
    else:
        if datetime.date(date1[0], date1[1], 1).weekday() == 6:
            counter+=1
    return counter
    
if __name__ == "__main__":
    t = int(input())
    
    for x in range(t):
        date1=list(map(int, input().split()))
        date2=list(map(int, input().split()))
        yeardiff = date2[0]-date1[0]
        date1[0] = date1[0] % 400 + 2000
        date2[0] = date1[0] + yeardiff

        print(firstSundays(date1, date2))