# Binet's formula to determine nth fibonacci number

import math

n = int(input())

def binet(n):
	return int((((1+math.sqrt(5))**n)-((1-math.sqrt(5))**n))/((2**n)*math.sqrt(5)))

for i in range(n):
	print(binet(i))