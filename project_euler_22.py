n=int(input())
li=[]
for i in range(n):
    x=input()
    li.append(x)
li.sort()
n=int(input())
for i in range(n):
    x=input()
    u=0    
    for i in x:
        u+=ord(i)-64
    a=li.index(x)
    print((a+1)*u)

# Input
# 5
# ALEX
# LUIS
# JAMES
# BRIAN
# PAMELA
# 1
# PAMELA