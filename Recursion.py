#Recursion : functions calling other function inside its definition

def myfunction1():
    myfunction2()
    print("function 1 is called")

def myfunction2():
    print("function 2 is called")

def functionNumber(num):
    if(num == 0):
        return
    print(num)
    functionNumber(num-1)

functionNumber(3)

# def factorial(num):
#     fact = 1;
#     for i in range(1, num+1):
#         fact = fact * i;
#     return fact


# print(factorial(5))

# Recursive Approach 
def recFactorial(num):
    if(num == 0 or num == 1):
        return 1
    return num * recFactorial(num-1)

print(recFactorial(5))

def fibonnacci(num):
    if(num <= 0):
        return 0
    if(num == 1 or num == 2):
        return 1
    
    return fibonnacci(num-1) + fibonnacci(num-2)

print(fibonnacci(6))