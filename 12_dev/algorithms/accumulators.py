def joinElements(array, joinString):
    def recurse(index, resultSoFar):
        resultSoFar += array[index]
        if index == len(array) - 1:
            return resultSoFar
        else:
            return recurse(index + 1, resultSoFar + joinString)
    return recurse(0, '')

print(joinElements(['s','cr','t cod', ' :) :)'], 'e'))

