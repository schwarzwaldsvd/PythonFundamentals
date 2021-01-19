def logNumbers(start, end):
    print(f"iteratively looping from {start} until {end}")
    for i in range(start,end+1):
        print(f'hitting index {i}')

def logNumbersRecursively(start, end):
    print(f'recursively looping from {start} until {end}')
    
    def recurse(i):
        print(f'hitting index {i}')
        if i < end:
            recurse(i+1)
    
    recurse(start)

print('- - logNumbers - -')
logNumbers(1,2)

print('- - logNumbersRecursively - -')
logNumbersRecursively(1,3)
