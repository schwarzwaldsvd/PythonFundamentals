from math import sqrt
from pprint import pprint as pp

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

def get_primes(number):
    return [x for x in range(number) if is_prime(x)]

def prime_square_divisors(number):
    result = {x*x:(1, x, x*x) for x in range(number) if is_prime(x)}
    return pp(result)