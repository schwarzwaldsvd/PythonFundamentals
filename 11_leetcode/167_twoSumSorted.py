"""
Given an array of integers that is already sorted in ascending order, 
find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such 
that they add up to the target, where index1 must be less than index2.

Note:
Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
 

Example 1:
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
"""

numbers = [2,3,4,7,10,11,15,23,34,45]
numbers.sort()
target = 9

class Solution:
    # two-pointer
    def twoSum1(self, nums, target):
        l = 0
        r = len(nums)-1
        while l < r:
            s = nums[l] + nums[r]
            if s == target:
                return [l+1, r+1]
            elif s < target:
                l += 1
            else:
                r -= 1
        return []

    # dictionary
    def twoSum2(self, nums, target):
        dic = {}
        for i, k in enumerate(nums):
            if target-k in dic:
                return [dic[target-k]+1, i+1]
            dic[k] =i
        return []

    # binary search iterative
    def twoSum3(self, nums, target):
        for i in range(len(nums)):
            l = i+1
            r = len(nums)-1
            compliment = target - nums[i]
            while l <= r:
                mid = l + (r-l)//2
                if nums[mid] == compliment:
                    return [i+1, mid+1]
                elif nums[mid] < compliment:
                    l = mid+1
                else:
                    r = mid-1
        return []

    # binary search recursive
    def twoSum4(self, nums, target, l, r):
        for i in range(len(nums)):
            if l > r:
                return []
            else:
                compliment = target - nums[i]
                mid = l + (r-l)//2
                if nums[mid] == compliment:
                    return [i+1, mid+1]
                elif nums[mid] < compliment:
                    return self.twoSum4(nums, target, mid+1, r)
                else:
                    return self.twoSum4(nums, target, l, mid-1)
        return []

s = Solution()
print("numbers =", numbers)
print("target =", target)
print("Answer:")

print(s.twoSum1(numbers, target))
print(s.twoSum2(numbers, target))
print(s.twoSum3(numbers, target))
print(s.twoSum4(numbers, target, 0, len(numbers)-1))

assert s.twoSum1(numbers, target) == [1 ,4] 
assert s.twoSum2(numbers, target) == [1 ,4] 
assert s.twoSum3(numbers, target) == [1 ,4] 