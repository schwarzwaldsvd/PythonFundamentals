"""Example:
    A = [1, 3, 11, 2, 7]
    target = 9
    return : [3, 4]

9 - 1 = 8 -> {8 : 0}
9 - 3 = 6 -> {8 : 0, 6 : 1}
9 - 11 = -2 -> {8 : 0, 6 : 1, -2 : 2}
9 - 2 = 7 -> {8 : 0, 6 : 1, -2 : 2, 7 : 3}

nums[i], i

"""


class Solution:
    def twoSum(self, A, target):
        if len(A) > 1:
            ht = dict()
            for i, v in enumerate(A):
                if v in ht:
                    return [ht[v], i]
                else:
                    ht[target - v] = i
        return []

    def twoSumSorted(self, A, target):
        A.sort()
        i = 0
        j = len(A) - 1
        while i < j:
            if A[i] + A[j] == target:
                return [i, j]
            elif A[i] + A[j] < target:
                i += 1
            else:
                j -= 1
        return []


s = Solution()
"""
print(s.twoSum([1, 3, 11, 2, 7], 9))  # Output: [3,4]
print(s.twoSum([2, 7, 11, 15], 9))  # Output: [0,1]
print(s.twoSum([3, 2, 4], 6))  # Output: [1,2]
print(s.twoSum([3, 3], 6))  # Output: [0,1]
print(s.twoSum([], 27))  # Output: []
print(s.twoSum([2, 7, 11, 15], 26))  # Output: [2, 3]
"""

print(s.twoSumSorted([1, 2, 3, 7, 11], 9))  # Output: [1, 3]
print(s.twoSumSorted([2, 7, 11, 15], 9))  # Output: [0,1]
print(s.twoSumSorted([2, 3, 4], 6))  # Output: [0,2]
print(s.twoSumSorted([3, 3], 6))  # Output: [0,1]
print(s.twoSumSorted([], 27))  # Output: []
print(s.twoSumSorted([2, 7, 11, 15], 26))  # Output: [2, 3]
