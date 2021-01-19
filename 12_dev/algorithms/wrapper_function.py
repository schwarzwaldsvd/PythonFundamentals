def wrapperFnLoop(start, end):
    def recurse(i):
        print(f'looping from {start} until {end}')
        if i< end:
            recurse(i+1)
    recurse(start)

def MemoFnLoop(i, end):
    print(f'looping from {i} until {end}')
    if i < end:
        MemoFnLoop(i + 1, end)

print('- - wrapperFnLoop - -')
wrapperFnLoop(1,5)
print('- - MemoFnLoop - -')
MemoFnLoop(1, 6)
