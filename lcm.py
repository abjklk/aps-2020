# Program to find LCM of n numbers using Euclid's GCD algorithm

from functools import reduce

a = 84
b = 72

def lcm(*args):
    numbers = list(args)

    def _gcd(x, y):
        return x if not y else _gcd(y, x % y)

    def _lcm(x, y):
        return x * y / _gcd(x, y)

    return reduce((lambda x, y: _lcm(x, y)), numbers)

print(lcm(a,b,10,12,8))