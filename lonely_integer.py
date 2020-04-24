# Finding the lonely integer in the sequence (the integer that only occurs once in the array).

# Input:
# 3
# 1 1 2
# 5
# 0 0 1 2 1

def lonelyinteger(a):
    res=0
    for i in a:
        res^=i
    return res

n = int(input())
a = list(map(int, input().strip().split()))
print(lonelyinteger(a))