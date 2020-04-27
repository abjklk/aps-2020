# Union Find Path Compression
# Union Time Complexity : O(logN)
def initialize(n): 
    global Arr, size 
    for i in range(n + 1): 
        Arr[i] = i  
        size[i] = 1

def _union(xr, yr): 
    global Arr, size 
    if (size[xr] < size[yr]): # Make yr parent of xr  
        Arr[xr] = Arr[yr]  
        size[yr] += size[xr] 
    else: # Make xr parent of yr 
        Arr[yr] = Arr[xr]  
        size[xr] += size[yr] 

def find(i): 
    global Arr, size 
    while (Arr[i] != i): 
        Arr[i] = Arr[Arr[i]] # Skip one level  
        i = Arr[i] # Move to the new level 
    return i 
  
