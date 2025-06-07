# Lists in Python 

myList = [10, 20, 30, 40, 50]
print(myList[0])
print(myList[1])

print(len(myList))


#taking list as an input from the user
# myList1 = []
# number = int(input())
# for i in range(0, number):
#     currElement = int(input())
#     myList1.append(currElement)

# print(myList1, type(myList1))

mylist2 = input().split(" ")
print(mylist2)

print(type(mylist2))


for i in range(len(mylist2)):
    mylist2[i] = int(mylist2[i])

print(mylist2, type(mylist2))
