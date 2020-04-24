# Sieve of Eratosthenes to find all primes from 2 to n
# Time Complexity : O(nloglogn) ~ O(n)
# if sieve[k] != 0 ==> k is not prime.
n=int(input())
sieve=[0]*(n+1)
for i in range(2,n+1):
	if sieve[i]:
		continue
	for j in range(2*i,n+1,i):
		sieve[j]=i
print(sieve)