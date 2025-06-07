#Calculating the mean median mode

number = int(input())
mylist = input().split(" ")

for i in range(len(mylist)):
    mylist[i] = int(mylist[i])

def meanFunction(mylist):
    meansum = 0;
    for val in mylist:
        meansum = meansum + val;

    mean = meansum/len(mylist)
    return mean

def meadianFunction(mylist):
    mylist.sort()
    if(number % 2 == 1):
        return mylist[number//2]
    
    else:
        return ((mylist[(number//2) - 1]) + mylist[number//2])/2


def mode(mylist):
    maxCount = 0
    maxELe = mylist[0]
    
    for  curEle in mylist:
        curCount = 0;
        for eachEle in mylist:
            if eachEle == curEle:
                curCount = curCount + 1
 
        if curCount > maxCount:
                maxELe = curEle
                maxCount = curCount
    return (maxELe, maxCount)

# Calculating the mean of the numbers
print(meanFunction(mylist))
print(meadianFunction(mylist))
print(mode(mylist))

