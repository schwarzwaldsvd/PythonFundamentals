def compute_factorial(num):
    result = 1
    
    for i in range(2,num+1):
        print(f"result = {result} * {i} ({result * i})")
        result *= i

    return result

print(compute_factorial(5))