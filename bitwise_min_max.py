# Given 2 numbers x and y find the min(x,y) and max(x,y) with bitwise ops

x=100
y=20
nmin = (y^(x^y)&-(x<y))
nmax = (x^(x^y)&-(x<y))
print(nmin)
print(nmax)