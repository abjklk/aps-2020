# Program to perform string.upper() using bitwise ops

a = "hello everyone"
x = ""

for i in a:
	x+=chr(ord(i) & ~32)
print(x)

# OR

print(a.upper())