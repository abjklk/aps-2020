# Scenario :
# if x == a:
# 	x = b
# or
# if x == b:
# 	x = a
# Accomplished using bitwise ops

a = 5
b = 6
x=100
x ^= a ^ b
print(x)