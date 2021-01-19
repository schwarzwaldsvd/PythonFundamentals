"""
Task 1: Without peeking, write your own recursive factorial method
Task 2: Use your memo function from the previous exercise to memoize your factorial method
"""

memo = {}

def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)

print(factorial(5))