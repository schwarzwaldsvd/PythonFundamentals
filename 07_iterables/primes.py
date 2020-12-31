from math import sqrt
from pprint import pprint as pp
from itertools import islice, count

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

def thousand_primes():
    return islice((x for x in count() if is_prime(x)), 1000)


# print(sum(x for x in range(1001) if is_prime(x)))
# print(list(thousand_primes()))
print(sum(thousand_primes()))

print(any(is_prime(x) for x in range(1328, 1361)))


