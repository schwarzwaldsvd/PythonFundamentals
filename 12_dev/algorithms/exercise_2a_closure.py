"""
Task 3: Clean up your global scope by moving your cache inside your function.
protip: Use a closure to return a function that you can call later.
"""

def memoizedClosureTimes10():
    cache = {}

    def closureTimes10(n):
        if n in cache:
            print("Fetching from cache:", n)
            return cache[n]
        else:
            print("Calculating result")
            result = n*10
            cache[n] = result
            return result
    
    return closureTimes10

memoClosureTimes10 = memoizedClosureTimes10()

try:
    print('~~~~~~~~~~~~~~ TASK 3 ~~~~~~~~~~~~~~')
    print('Task 3 calculated value:', memoClosureTimes10(9))	# calculated
    print('Task 3 cached value:', memoClosureTimes10(9))	    # cached
except Exception as e:
    print("Error:", e)
finally:
    print("Done") 