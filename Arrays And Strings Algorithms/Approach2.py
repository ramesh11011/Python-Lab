#Kadane's Algorithm Practice 

import sys

arr = [int(ele) for ele in input().split()]


def kadane(arr):
    start = -sys.maxsize-1
    end = 0
    curSum = 0
    maxSum = 0

    n = len(arr)

    while end < n:
        while curSum < 0:
            curSum -= arr[start]
            start += 1
        
        curSum += arr[end]
        end += 1

        maxSum = max(curSum, maxSum)

    return maxSum

# Maximum sum of sub array

def maxfunction(arr):
    currsum = arr[0]
    maxSum = arr[0]

    n = len(arr)
    for i in range(1, n):
        currsum = max(arr[i], currsum+arr[i])
        maxSum = max(currsum, maxSum)

    return maxSum