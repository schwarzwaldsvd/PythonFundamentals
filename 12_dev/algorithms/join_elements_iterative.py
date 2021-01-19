""" Task: rewrite this function so that it uses a loop rather than recursion """

def joinElements(array, joinString):
    resultSoFar = ''
    for i in range(len(array)-1):
        resultSoFar += array[i] + joinString
    return resultSoFar + array[len(array)-1]

print(joinElements(['s','cr','t cod', ' :) :)'], 'e'))
