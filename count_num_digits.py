# Program to determine the number of digits in a number in logn time

import math

n = 1029743
print(math.floor(math.log10(n)+1))

# or
print(len(str(n)))