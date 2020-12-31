from itertools import chain

sunday = [12, 14, 15, 15, 17, 21, 22, 22, 23, 22, 20, 10]
monday = [13, 14, 14, 14, 16, 20, 21, 22, 22, 21, 19, 17]
tuesday = [2, 2, 3, 7, 9, 10, 11, 12, 10, 9, 8, 8]

def combine():
    for item in zip(sunday, monday):
        print(item)

def average():
    for sun, mon in zip(sunday, monday):
        print("average = ", (sun + mon) /2 )


def stats():
    for temps in zip(sunday, monday, tuesday):
        print("min={:4.1f}, max={:4.1f}, average={:4.1f}".format(min(temps), max(temps), sum(temps)/len(temps)))

def check_temp(temperature):
    temperatures = chain(sunday, monday, tuesday)
    return all(t > temperature for t in temperatures)

combine()
average()
stats()

print(check_temp(0))