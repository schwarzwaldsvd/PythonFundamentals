from math import factorial
words = "Why sometimes I have believed as many as six impossible things before breakfast".split()

def print_words_lengths1():
    return [len(word) for word in words]

def print_words_lengths2():
    lengths = []
    for word in words:
        lengths.append(len(word))
    return lengths

def print_fac_lengths(number):
    return [len(str(factorial(x))) for x in range(number)]

def print_fac_lengths_set(number):
    return {len(str(factorial(x))) for x in range(number)}
