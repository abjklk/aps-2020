import math 
  
def highestPowerof2(n): 
  
    p = int(math.log(n, 2)) 
    return int(pow(2, p))
  
# Driver code 
n = 10
print(highestPowerof2(n))