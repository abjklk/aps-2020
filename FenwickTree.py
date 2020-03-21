# Fenwick Tree a.k.a indexed binary tree
n=10
fenwick=[0]*(n+1)

def update(ind,val,a):
	global n
	global fenwick
	while(ind<=max(a)):
		fenwick[ind]+=val
		print(fenwick)
		ind+=ind&-ind

def query(x):
	global n
	global fenwick
	qsum=0
	while(x>0):
		qsum+=fenwick[x]
		x-=x&-x
	return qsum

def rangeq(a,b):
	return query(b)-query(a)


a=[1]*n
for i in range(n):
	update(i+1,a[i])

print(query(5))
print(query(4))
print(query(10))
print(rangeq(5,10))