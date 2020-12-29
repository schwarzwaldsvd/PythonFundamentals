"""Given an array of integers 'nums' and an integer 'target', 
return indices of the two numbers such that they add up to 'target'.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

You can return the answer in any order.
"""


class Solution:
    def twoSum(self, nums, target):
        compliments = {}
        result = []
        for index, value in enumerate(nums):
            if compliments.get(value) is None:
                compliments[target - value] = index
            else:
                result = [compliments[value], index]
        return result


l = Solution()
print(l.twoSum([2, 7, 11, 15], 9))  # Output: [0,1]
print(l.twoSum([3, 2, 4], 6))  # Output: [1,2]
print(l.twoSum([3, 3], 6))  # Output: [0,1]
print(l.twoSum([], 27))  # Output: []
print(l.twoSum([2, 7, 11, 15], 26))  # Output: [2, 3]

'''
Example walkthrough...
compliments = {24: 0, 19: 1, 15: 2}
compliments[15] = 2, 3
results = [2, 3]
'''
