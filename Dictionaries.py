#Dictionaries in Python

myDict = {"Studen1" : 90, "Student2" : 98, "Student3" : 42}
print(myDict.items())
print(myDict.keys())
print(myDict.values())

for val in myDict.values():
    print(val)

    
targetKey = "student1"
if targetKey in myDict:
    print("present")

print(myDict)