# collection
cities = ["London", "Newy York", "Paris", "Oslo", "Chișinău"]
for city in cities:
    print(city)


# dictionary
nums = dict()
nums = {1 : 'one', 2: 'two', 3 : 'three', 4 : 'four', 5 : 'five'}

for index, value in enumerate(nums):
    print(index, value, nums[value])

colors = {'crimson' : 0xdc143c, 'coral' : 0xff7450, 'teal' : 0x008080 }
for color in colors:
    print(color, colors[color])


print(colors.get('crimson'))