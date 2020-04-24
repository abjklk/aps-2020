# Sparse Table
import math

a=[7,3,2,4,0,1,5,8,2,4] 
n=10
l=[[0]*(int(math.log2(n))+1) for i in range(n)]
for i in range(n):
	l[i][0]=i

j=1
while((1<<j)<=n):
	i=0
	while((i+(1<<j)-1)<n):
		if a[l[i][j-1]] > a[l[i+(1<<(j-1))][j-1]]:
			l[i][j]=l[i][j-1]
		else:
			l[i][j]=l[i+(1<<(j-1))][j-1]
		i+=1
	j+=1
print(l)

def query(a,le,ri):
	global l
	j=int(math.log2(ri-le+1))
	if a[l[le][j]]>=a[l[ri-(1<<j)+1][j]]:
		return a[l[le][j]]
	else:
		return a[l[ri-(1<<j)+1][j]]
print(query(a,0,2))
