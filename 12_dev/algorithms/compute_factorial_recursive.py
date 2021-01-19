def compute_factorial(num):
    if num == 1:
        print('hitting the base case')
        return 1
    else:
        print(f'returning {num} * compute_factorial({num - 1})')
        return num * compute_factorial(num - 1)
print(compute_factorial(5))