# How to unset ith bet in a given number n?

n = 8  #1000
tounset = 3
n &= ~(1 << tounset) #1100
print(n)  