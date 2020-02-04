# Program to generate all combinations of a string/list
# r-> 0-> n
from itertools import combinations

s=input()
for i in range(1,len(s)+1):
	for j in combinations(s,i):
		print("".join(j))
