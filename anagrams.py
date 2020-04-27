# Program to determine whether a pair of words are anagrams or not using Counter

from collections import Counter
x = "abcd"
y = "dcba"
print(Counter(x)==Counter(y))
