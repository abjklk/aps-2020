import random

def matrix_gen():
	m = [chr(i) for i in range(65,91)]+[i for i in range(0,10)]
	random.shuffle(m)
	matrix = []
	for i in range(0,36,6):
		matrix.append(m[i:i+6])
	return matrix

def key_sort(key):
	key = list(key)
	key.sort()
	return "".join(key)

def spread(arr):
	res = []
	for i in arr:
		if isinstance(i,list) or isinstance(i,tuple):
			res.extend(i)
		else:
			res.append(i)
	return res

matrix = [['P', 'M', 'D', '1', 'O', 'W'], ['T', 'C', 'Z', 'J', 'Q', 'R'], ['X', '8', '2', 'H', 'S', 'A'], ['0', 'E', '9', 'L', 'V', 'K'], ['G', '7', 'Y', '4', 'B', 'U'], ['6', 'F', '3', 'N', 'I', '5']]
key = "LIFE"
cipher = "DAAXVXAGVAXAG-GDDFFADVADFGV-GDVVXAVGVXVAAAGXFGFDXFVFFDGG"
adfgvx = {"A":0,"D":1,"F":2,"G":3,"V":4,"X":5}
decipher= ""
# Get sorted key
skey = key_sort(key)

# Generate key table
key_table = []
for i in range(0,len(cipher),len(cipher)//len(key)):
	key_table.append(list(cipher[i:i+len(cipher)//len(key)]))

# Transpose key table
key_table = list(zip(*key_table))
key_table.insert(0,list(skey))
# print(key_table)

# Rearrange key table based on key
key_table = list(zip(*key_table))
# print(key_table)
kt2 = [0]*len(key)
for i in key_table:
	kt2[key.index(i[0])]=i
key_table = list(zip(*kt2))

# Get encoded string
key_table.pop(0)
key_table = "".join(spread(key_table))
key_table = key_table.replace('-','')
# print(key_table)
for i in range(0,len(key_table),2):
	decipher+=(matrix[adfgvx[key_table[i]]][adfgvx[key_table[i+1]]])

print(decipher)