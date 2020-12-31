from math import sqrt


def fibonacci():
    yield 2
    a = 2
    b = 1
    while True:
        yield b
        a, b = b, a + b


def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


def print_fibonacci():
    for x in fibonacci():
        print(x)


def print_primes_in_fibonacci():
    for x in (p for p in fibonacci() if is_prime(p)):
        print(x)


print_primes_in_fibonacci()