# Program to determine highest power of 2 less than or equal to n.
import math 
  
def highestPowerof2(n): 
  
    p = int(math.log(n, 2)) 
    return int(pow(2, p))
  
n = 10
print(highestPowerof2(n))