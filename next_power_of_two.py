# Program to determine the next power of 2 greater than or equal to n.
def nextPowerOf2(n): 
  
    n -= 1
    n |= n >> 1
    n |= n >> 2
    n |= n >> 4
    n |= n >> 8
    n |= n >> 16
    n += 1
    return n

n = 6
print(nextPowerOf2(n)) 