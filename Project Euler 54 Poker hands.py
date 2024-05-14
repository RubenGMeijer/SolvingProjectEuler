
def stringToValues(hand):
    values=[]
    for x in range(0, 15, 3):
        if hand[x] == 'T':
            values.append(10)
        elif hand[x] == 'J':
            values.append(11)
        elif hand[x] == 'Q':
            values.append(12)
        elif hand[x] == 'K':
            values.append(13)
        elif hand[x] == 'A':
            values.append(14)
        else:
            values.append(int(hand[x]))
    values.sort(reverse=True)
    colour=hand[1]                  # Flush determined here
    for x in range(4, 15, 3):
        if hand[x] != colour:
            values.append(0)
            break
    else:
        values.append(5)
    return values

def straight(values):
    if values[0:5] == [14, 5, 4, 3, 2]:  # in straight, Ace can be highest or lowest
        values[0:5] = [5, 4, 3, 2, 1]
    for x in range(1, 5):
        if values[x-1] != values[x]+1:
            break
    else:
        values[5]+=4
    return values

def pairing(values):
    currentValue=0
    currentStreak=1
    pairs=[]
    
    for x in range(5):
        if currentValue == values[x]:
            currentStreak+=1
        else:
            if currentStreak>1:
                pairs.append([currentStreak, currentValue])
            currentValue = values[x]
            currentStreak=1
    else:
        if currentStreak>1:
            pairs.append([currentStreak, currentValue])
    while len(pairs) < 2:
        pairs.append([0, 0])
        
    pairs.sort(reverse=True)
    
    if pairs[0][0] == 4:
        values[5] += 7
    elif pairs[0][0] == 3:
        if pairs[1][0] == 2:
            values[5] +=6
        else:
            values[5] +=3
    elif pairs[0][0] == 2:
        if pairs[1][0] == 2:
            values[5] +=2
        else:
            values[5] +=1
    
    # Sort cards: pairs first for compareHighCard
    oldValues=values[0:5]
    newValues=[]
    while pairs[0][0]:
        pairs[0][0]-=1
        newValues.append(pairs[0][1])
        oldValues.remove(pairs[0][1])
    while pairs[1][0]:
        pairs[1][0]-=1
        newValues.append(pairs[1][1])
        oldValues.remove(pairs[1][1])
    newValues+=oldValues
    newValues.append(values[5])
    return newValues

def compareHighCard(values1, values2):     # determine which card is highest for tiebreaks
    for x in range(5):
        if values1[x] > values2[x]:
            return 1
        if values1[x] < values2[x]:
            return 2
    return 0

def winner(hand1, hand2):
    values1=pairing(straight(hand1))
    values2=pairing(straight(hand2))
    # syntax: Cards 1 2 3 4 5 CombinationValue
    # index:        0 1 2 3 4 5
    
    if values1[5] > values2[5]:
        return 1
    if values1[5] < values2[5]:
        return 2
    return compareHighCard(values1, values2)

if __name__ == "__main__":
    t=int(input())
    for x in range(t):
        hands = input()
        hand1 = stringToValues(hands[0:15])
        hand2 = stringToValues(hands[15:])
        print("Player "+str(winner(hand1, hand2)))
        
        
