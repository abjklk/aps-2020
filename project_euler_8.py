t = int(input().strip())
for _ in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    num = input().strip()
    li=[0]
    for i in range(n-k):
        pr=1
        for j in num[i:i+k]:
            pr*=int(j)
            if pr==0:
                break
        li.append(pr)
    print(max(li))

# Input
# 2
# 10 5
# 3675356291
# 10 5
# 2709360626