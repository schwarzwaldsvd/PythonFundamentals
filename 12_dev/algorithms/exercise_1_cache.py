"""
Task 1: Write a function, times10, that takes an argument, n, and multiples n times 10
a simple multiplication fn
"""
def times10(n):
    return n*10

print('~~~~~~~~~~~~~~ TASK 1 ~~~~~~~~~~~~~~')
print('times10 returns:', times10(9))

"""
Task 2: Use an object to cache the results of your times10 function. 
protip 1: Create a function that checks if the value for n has been calculated before.
protip 2: If the value for n has not been calculated, calculate and then save the result in the cache object.
"""

cache = {}

def memoTimes10(n):
    print(cache)
    if n in cache:
        print("Fetching from cache:", n)
        return cache[n]
    else:
        print("Calculating result")
        result = times10(n)
        cache[n] = result
        return result

print('~~~~~~~~~~~~~~ TASK 2 ~~~~~~~~~~~~~~')
print('Task 2 calculated value:', memoTimes10(9))	# calculated
print('Task 2 cached value:', memoTimes10(9))	    # cached