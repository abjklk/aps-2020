# Program to print nth catalan number using recursion

def catalan_rec(n):
    if n<=1:
        return 1
    res=0
    for i in range(n):
        res += catalan_rec(i)*catalan_rec(n-i-1)
    return res

n = 10
print(catalan_rec(n))
