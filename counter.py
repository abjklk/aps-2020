# Counter takes an iterable and returns an Counter object with the iterable as key and its no. of occurence as the value

from collections import Counter

a=[1,1,1,1,1,2,2,2,3,4,5,66,3,1,2,1,5,57,65,36,36,88]
print(dict(Counter(a)))