#Largest Subarray Sum (Kadane's Algorithm)

def LargestSubarraySum(arr):
    currSum = arr[0]   
    maxsum = arr[0]

    for i in range(1, len(arr)):
        currSum = max(currSum + arr[i], arr[i])
        maxsum = max(currSum, maxsum)
    return maxsum


if __name__ == "__main__":
    arr = [2,3,-8,7,-1,2,3]
    print(LargestSubarraySum(arr))

