def loopNTimes(n):
    print(f"n = {n}")
    if n<= 1:
        return 'complete'
    return loopNTimes(n-1)

print(loopNTimes(3))