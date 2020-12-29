"""Example:
    nums = [1, 3, 11, 2, 7]
    target = 9
    return : [3, 4]

9 - 1 = 8 -> {8 : 0}
9 - 3 = 6 -> {8 : 0, 6 : 1}
9 - 11 = -2 -> {8 : 0, 6 : 1, -2 : 2}
9 - 2 = 7 -> {8 : 0, 6 : 1, -2 : 2, 7 : 3}

nums[i], i

"""


class Solution:
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return []
        compliments = {}
        for i in range(len(nums)):
            if nums[i] in compliments:
                return [compliments[nums[i]], i]
            else:
                compliments[target - nums[i]] = i


s = Solution()
print(s.twoSum([1, 3, 11, 2, 7], 9))  # Output: [3,4]
print(s.twoSum([2, 7, 11, 15], 9))  # Output: [0,1]
print(s.twoSum([3, 2, 4], 6))  # Output: [1,2]
print(s.twoSum([3, 3], 6))  # Output: [0,1]
print(s.twoSum([], 27))  # Output: []
print(s.twoSum([2, 7, 11, 15], 26))  # Output: [2, 3]
