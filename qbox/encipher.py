adfgvx = "ADFGVX"
key = "GERMANY"
matrix = [['P', 'M', 'D', '1', 'O', 'W'], ['T', 'C', 'Z', 'J', 'Q', 'R'], ['X', '8', '2', 'H', 'S', 'A'], ['0', 'E', '9', 'L', 'V', 'K'], ['G', '7', 'Y', '4', 'B', 'U'], ['6', 'F', '3', 'N', 'I', '5']]

# Input Message
text = "ATTACKATDAWN"
c = ""
cipher = ""

# Generate encode 1
for k in text:
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			if matrix[i][j]==k:
				c += adfgvx[i]
				c += adfgvx[j]
				break
# print(c)

# Append '-' if necessary
if len(c)%len(key):
		# print('mod',len(c)%len(key))
	c+="-"*(len(key)-(len(c)%len(key)))

# Initialize and build key table
key_table = [key]
for i in range(0,len(c),len(key)):
	key_table.append(c[i:i+len(key)])
# print(key_table)

# Transpose and sort key table
key_table = list(zip(*key_table))
# print(key_table)
key_table.sort()
# print(key_table)

# Obtain cipher text from key table
cipher += "".join("".join(i[1:]) for i in key_table)

print("Input String :",text)
print("matrix :\n",matrix)
print("Key :",key)

print("Encoded Text :",cipher)
