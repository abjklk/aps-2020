# Python program to demonstrate stack implementation using collections.deque 
from collections import deque 

stack = deque() 

# append() function
stack.append('a') 
stack.append('b') 
stack.append('c') 

print('Initial stack:') 
print(stack) 

# pop() fucntion LIFO
print('Elements poped from stack:') 
print(stack.pop()) 
print(stack.pop()) 
print(stack.pop()) 

print('Stack after elements are popped:') 
print(stack) 
