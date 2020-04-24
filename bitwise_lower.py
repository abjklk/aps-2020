a = "HELLO EVERYONE"
x = ""

for i in a:
	x+=chr(ord(i) | 32)
print(x)

# OR

print(a.lower())