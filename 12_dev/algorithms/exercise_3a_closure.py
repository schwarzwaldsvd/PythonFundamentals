"""
Task 4: Make your memo function generic and accept the times10 function as a callback rather than defining the n * 10 logic inside the if/else or pulling it in from the global scope.
protip: Take advantage of the fact that parameters are saved in the closure as well, just like the cache from the previous example.

returned function from memoizedAdd

"""

def times10(n):
    return n*10

def memoize(cb):
    cache = {}

    def closure(n):
        if n in cache:
            print("Fetching from cache:", n)
            return cache[n]
        else:
            print("Calculating result")
            result = cb(n)
            cache[n] = result
            return result
    
    return closure

memoClosureTimes10 = memoize(times10)

try:
    print('~~~~~~~~~~~~~~ TASK 4 ~~~~~~~~~~~~~~')
    print('Task 4 calculated value:', memoClosureTimes10(9))	# calculated
    print('Task 4 cached value:', memoClosureTimes10(9))	    # cached
except Exception as e:
    print("Error:", e)
finally:
    print("Done") 