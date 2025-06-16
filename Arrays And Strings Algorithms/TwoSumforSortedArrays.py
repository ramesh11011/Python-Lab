# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         nums.sort()
#         start = 0
#         end = len(nums) - 1
#         currSum = 0

#         while start < end:
#             currSum = nums[start] + nums[end]
#             if currSum == target:
#                 return [start,end]

#             if currSum > 0:
#                 end -= 1
#             else:
#                 start += 1

#         return -1


# Code for implementation of the two sum problem