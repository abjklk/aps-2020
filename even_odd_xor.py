# Given a sequence A1,A2,…,AN and Q queries. 
# In each query, the student is given an integer P; 
# construct a sequence B1,B2,…,BN, where P xor Ai=Bi 
# for each valid i, find the number of elements of this sequence which have an even number of 1-s 
# in the binary representation and the number of elements with an odd number of 1-s in the binary representation.

# Codechef Problem code : ENGXOR

# Input:
# 1
# 6 1
# 4 2 15 9 8 8
# 3
from sys import stdin,stdout

def c(n):
    n=int(n)
    if bin(n).count("1")&1:
        return 1
    return 0

t=int(input())
for _ in range(t):
    x=list(map(int,input().split()))
    li=list(map(c,stdin.readline().split()))
    su=sum(li)
    zq=(x[0]-su,su)
    oq=zq[::-1]
    for _ in range(x[1]):
        q=int(stdin.readline())
        if bin(q).count("1")&1:#even no of 1s
            print(*oq)
        else:#odd
            print(*zq)
    