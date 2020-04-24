# Python snippets to find various sums of series

n = 58
# Sum of first n numbers
ans = (n*(n+1))//2
print(ans)

# Sum of first n squared numbers
ans = (n*(n+1)*(2*n+1))//6
print(ans)

# Sum of first n cubed numbers
ans = ((n**2)*(n+1)**2)//4
print(ans)