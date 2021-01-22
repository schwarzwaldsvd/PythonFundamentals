"""
Task 1: Without peeking, write your own recursive factorial method
Task 2: Use your memo function from the previous exercise to memoize your factorial method
"""

def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)

def memoize(cb):
    cache = {}

    def closure(num):
        if num in cache:
            print("Fetching from cache", num)
            return cache[num]
        else:
            print("Calculating result")
            result = cb(num)
            cache[num] = result
            return result
    return closure

memoClosureFactorial = memoize(factorial)

print(memoClosureFactorial(5))
print(memoClosureFactorial(5))
# check if factorial(5) is cached, if so, then return factorial(5)*6
print(memoClosureFactorial(6))
print(memoClosureFactorial(6)) 
