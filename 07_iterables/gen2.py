hundred_squares = (x*x for x in range(1, 100))
print(list(hundred_squares))

# 
s = sum(x*x for x in range(1, 10000))
print(s)