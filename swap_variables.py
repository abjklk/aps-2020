# Given two Variables a and b swap the contents of a and b without another variable.

a = 65
b = 37
# Arithmetic Method
a = a+b
b = a-b
a = a-b
print(a,b)

# Using Xor
a = a ^ b
b = a ^ b
a = a ^ b
print(a,b)

# Python way

a, b = b, a
print(a,b)