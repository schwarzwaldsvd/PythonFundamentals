"""
Task 3: Clean up your global scope by moving your cache inside your function.
protip: Use a closure to return a function that you can call later.
"""

def memoizedClosureTimesM(m):
    cache = {}

    def closureTimesM(n):
        if n in cache:
            print("Fetching from cache:", n)
            return cache[n]
        else:
            print("Calculating result")
            result = n*m
            cache[n] = result
            return result
    
    return closureTimesM

# there will be 2 (two) separate 'cache' variables,
# 1 for 'memoizedClosureTimesM(10)' and 2 for 'memoizedClosureTimesM(5)'
memoClosureTimes10 = memoizedClosureTimesM(10)
memoClosureTimes5 = memoizedClosureTimesM(5)

try:
    print('~~~~~~~~~~~~~~ TASK 3 ~~~~~~~~~~~~~~')
    print('~~~~~~~~~~~~~ Times 10 ~~~~~~~~~~~~~')
    print('Task 3 calculated value:', memoClosureTimes10(9))	# calculated
    print('Task 3 cached value:', memoClosureTimes10(9))	    # cached
    print('~~~~~~~~~~~~~ Times 5 ~~~~~~~~~~~~~~')
    print('Task 3 calculated value:', memoClosureTimes5(9))	    # calculated
    print('Task 3 cached value:', memoClosureTimes5(9))	        # cached
except Exception as e:
    print("Error:", e)
finally:
    print("~~~~~~~~~~~~~~ Done ~~~~~~~~~~~~~~~") 