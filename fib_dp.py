# Fibonacci Sequence Generator using DP approach

def fib(n):
	fib=[0,1]
	for i in range(n):
		fib.append(fib[-1]+fib[-2])
	return fib

n=int(input())
x=fib(n)
print(x)