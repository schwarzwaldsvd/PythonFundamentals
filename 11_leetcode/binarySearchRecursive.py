numbers = [2,3,4,7,10,11,15,23,34,45]
numbers.sort()
target = 9

# binary search recursive
def twoSum(nums, target, l, r):
    for i in range(len(nums)):
        if l > r:
            return []
        else:
            #l = i+1
            #r = len(nums)-1
            compliment = target - nums[i]
            mid = l + (r-l)//2
            if nums[mid] == compliment:
                return [i+1, mid+1]
            elif nums[mid] < compliment:
                return twoSum(nums, target, mid+1, r)
            else:
                return twoSum(nums, target, l, mid-1)
                #r = mid-1
    return []

print("numbers =", numbers)
print("target =", target)
print("Answer:")
print(twoSum(numbers, target, 0, len(numbers)-1))

