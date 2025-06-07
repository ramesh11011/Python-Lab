# Basic Functions in Python 

def twoSum(num1, num2):
    return num1+num2

a = int(input("Enter the value of a : "))
b = int(input("Enter the value of a : "))
print(twoSum(a,b))

#dynamic function for adding numbers 
#creating Dynamic Function
def twoSum2(*number):
    # print(number)
    ans = 0;
    for itr in number:
        # print(itr, type(itr))
        ans = ans + itr;
    print(ans)

twoSum2(12, 13, 8, 12,45)