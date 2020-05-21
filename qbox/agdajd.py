'''a = open('bletchley.txt','r')
x = []
for i in a.readlines():
	if i!='\n':
		s=""
		for k in i:
			if k.isalnum():
				s+=k.upper()
		x.append(s)
a.close()
a = open('tc.txt','w+')
for i in x:
	a.write(i+'\n')
a.close()'''

'''
from collections import Counter

a = open('words.txt','r')
x = set()
for i in a.readlines():
	if len(Counter(i))==len(i):
		x.add(i[:-1].upper())
a.close()
print(x)
print(len(x))
a = open('key.txt','w+')
for i in x:
	a.write(i+'\n')
a.close()
'''
'''
import random

def matrix_gen():
	m = [chr(i) for i in range(65,91)]+[i for i in range(0,10)]
	random.shuffle(m)
	matrix = []
	for i in range(0,36,6):
		matrix.append(m[i:i+6])
	return matrix

a = open('matrix.txt','w+')
for i in range(80):
	a.write('\n'.join([' '.join([str(cell) for cell in row]) for row in matrix_gen()]))
	a.write('\n\n')
a.close()
'''

import random


def matrix_gen():
	m = [chr(i) for i in range(65,91)]+[str(i) for i in range(0,10)]
	random.shuffle(m)
	matrix = []
	for i in range(0,36,6):
		matrix.append(m[i:i+6])
	return matrix


def encipher(matrix,key,text):
	adfgvx = "ADFGVX"
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
	# print('encode1',c)

	# Append '-' if necessary
	if len(c)%len(key):
		# print('mod',len(c)%len(key))
		c+="-"*(len(key)-(len(c)%len(key)))

	# Initialize and build key table
	key_table = [key]
	for i in range(0,len(c),len(key)):
		key_table.append(c[i:i+len(key)])
	# print('ktab',key_table)

	# Transpose and sort key table
	key_table = list(zip(*key_table))
	# print(key_table)
	key_table.sort()
	# print('ktab2',key_table)

	# Obtain cipher text from key table
	cipher += "".join("".join(i[1:]) for i in key_table)

	# print(text)
	# print("matrix :\n",matrix)
	# print("Key :",key)

	# print(cipher)
	return cipher


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

def decipher(matrix,key,cipher):
	adfgvx = {"A":0,"D":1,"F":2,"G":3,"V":4,"X":5}
	decipher= ""
	# Get sorted key
	skey = key_sort(key)

	# Generate key table
	key_table = []
	for i in range(0,len(cipher),len(cipher)//len(key)):
		key_table.append(list(cipher[i:i+len(cipher)//len(key)]))
	# print(key_table)
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
	print(key_table)

	# Get encoded string
	key_table.pop(0)
	key_table = "".join(spread(key_table))
	key_table = key_table.replace('-','')
	# print(key_table)
	for i in range(0,len(key_table),2):
		decipher+=(matrix[adfgvx[key_table[i]]][adfgvx[key_table[i+1]]])

	# print(decipher)
	return decipher



# key = open('key.txt','r')
# tc = open('tc.txt','r')

# aa = open('input09.txt','w')
# bb = open('output09.txt','w') 


# for i in range(8):
# 	k = key.readline()[:-1]
# 	m = matrix_gen()
# 	# print(m)
# 	aa.write('\n'.join([' '.join([str(cell) for cell in row]) for row in m]))
# 	aa.write('\n')
# 	aa.write(k)
# 	aa.write('\n')
# 	txt = tc.readline()[:-1]
# 	ci = encipher(m,k,txt)
# 	de = decipher(m,k,ci)
# 	print(de == txt)
# 	aa.write(ci)
# 	aa.write('\n')
# 	bb.write(de)
# 	bb.write('\n')
# 	# print(txt)
# 	# en = cip.encipher(txt)
# 	# print(en)
# 	# print(cip.decipher(en))

# key.close()
# tc.close()
# aa.close()
# bb.close()

matrix = [['P', 'M', 'D', '1', 'O', 'W'], ['T', 'C', 'Z', 'J', 'Q', 'R'], ['X', '8', '2', 'H', 'S', 'A'], ['0', 'E', '9', 'L', 'V', 'K'], ['G', '7', 'Y', '4', 'B', 'U'], ['6', 'F', '3', 'N', 'I', '5']]


print(decipher(matrix,"GERMANY","DXF-XDAXFXDXAGF-AFX-DDAGFXA-"))

# key = "REPUBLIC"
matrix = [['P', 'M', 'D', '1', 'O', 'W'], ['T', 'C', 'Z', 'J', 'Q', 'R'], ['X', '8', '2', 'H', 'S', 'A'], ['0', 'E', '9', 'L', 'V', 'K'], ['G', '7', 'Y', '4', 'B', 'U'], ['6', 'F', '3', 'N', 'I', '5']]
# text = "LEFTSTVAASTWITH4BOATSAT0040"

# pp = encipher(matrix,key,text)
# decipher(matrix,key,pp)