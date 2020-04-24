# Python program of queue using deque
 
from collections import deque 
queue = deque([5,8,23,6,89]) 
print(queue) 
queue.append(90) 
print(queue) 
queue.append(45) 
print(queue) 

# O(1) pop time for popping index 0
print(queue.popleft())                  
print(queue.popleft())                  
print(queue) 