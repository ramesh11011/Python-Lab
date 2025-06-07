#Minimum and Maximum of the list
num = int(input())
mylist1 = input().split(" ")

 
for i in range(len(mylist1)):
    mylist1[i] = int(mylist1[i])

minElement = mylist1[0]
maxElement = mylist1[0]

for i in range(1,len(mylist1)):
    if(mylist1[i] > minElement):
        maxElement = mylist1[i]

    if(mylist1[i] < maxElement):
        minElement = mylist1[i]


#the same loop can be written as 
# for val in mylist1:
#     if val > maxElement:
#         maxElement = val
    
#     if val < minElement:
#         minElement = val

print(maxElement,minElement)
