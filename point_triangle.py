# Program to check whether point P(x, y) 
# lies inside the triangle formed by  
# A(x1, y1), B(x2, y2) and C(x3, y3)  

def area(x1, y1, x2, y2, x3, y3): 

    return abs((x1 * (y2 - y3) + x2 * (y3 - y1)  
                + x3 * (y1 - y2)) / 2.0) 
  
def isInside(x1, y1, x2, y2, x3, y3, x, y): 
  
    # Calculate area of triangle ABC 
    A = area (x1, y1, x2, y2, x3, y3) 
  
    # Calculate area of triangle PBC  
    A1 = area (x, y, x2, y2, x3, y3) 
      
    # Calculate area of triangle PAC  
    A2 = area (x1, y1, x, y, x3, y3) 
      
    # Calculate area of triangle PAB  
    A3 = area (x1, y1, x2, y2, x, y) 
      
    if(A == A1 + A2 + A3): 
        return True
    else: 
        return False

# A(0,0)
# B(20,0)
# C(30,10)
# P(10,15)
if (isInside(0, 0, 20, 0, 10, 30, 10, 15)): 
    print('Inside') 
else: 
    print('Not Inside')  