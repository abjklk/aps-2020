# Program to cyclic rotate an array using deque's rotate method
# deque.rotate(n)--> n right rotations
# deque.rotate(-n)--> n left rotations


from collections import deque

a = [1,2,3,4,5,6]
b = [1,2,3,4,5,6]
a = deque(a)
a.rotate(-3)
print(a)
b = deque(b)
b.rotate(2)
print(b)