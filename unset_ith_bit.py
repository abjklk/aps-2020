# How to unset ith bit in a given number n?

n = 8  #1000
tounset = 3
n &= ~(1 << tounset)
print(n)  