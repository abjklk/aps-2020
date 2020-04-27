# josephus problem given n

def josephus(n):
    res=0
    for i in range(n,0,-1):
        if (i&(i-1))==0:
            res=i
            break
    return res
n=int(input())
p=josephus(2*n)
print(2*n-p+1)