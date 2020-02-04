# Program to generate all permutations of a string/list
from itertools import permutations

s=input()

for i in permutations(s):
	print("".join(i))