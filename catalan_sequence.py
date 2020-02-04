# Dyck Path
# Dyck Sequences follow Catalan numbers.==> 1,1,2,5,42...
# Generates Catalan Sequence from {x,y} given input n.
from itertools import permutations

fl = 0
li=[]
la=[]
n=int(input())
st = "x"*n+"y"*n
for i in list(permutations(st)):
	z="".join(i)
	fl = 0
	for x in z:
		if x == "x":
			li.append(1)
		elif x=="y":
			try:
				li.pop()
			except:
				fl = 1
				break
	if fl==0:
		la.append(z)

print(list(set(la)))
print(len(set(la)))
