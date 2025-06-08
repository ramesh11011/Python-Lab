mystr = input()
countOne = mystr.count('1')
countZero = mystr.count('0')

# If the total number of 0s or 1s is odd, it's not possible
if countOne % 2 == 1 or countZero % 2 == 1:
    print(-1)
else:
    currOne = 0
    currZero = 0
    splitIndex = -1

    for i in range(len(mystr)):
        if mystr[i] == '1':
            currOne += 1
        else:
            currZero += 1
        
        # When both 0 and 1 reach half of their total counts
        if currOne == countOne // 2 and currZero == countZero // 2:
            splitIndex = i
            break

    if splitIndex != -1:
        print(mystr[:splitIndex + 1])
        print(mystr[splitIndex + 1:])
    else:
        print(-1)
