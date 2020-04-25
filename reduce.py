# Program to demonstrate working of reduce() along with operator functions 

# At first step, first two elements of sequence are picked and the result is obtained.
# Next step is to apply the same function to the previously attained result and the number just succeeding the second element and the result is again stored.
# This process continues till no more elements are left in the container.
# The final returned result is returned and printed on console.

import functools 
import operator 

lis = [1,4,62,6,16,4,6,7] 

# Sum
print (functools.reduce(operator.add,lis)) 

# Product
print (functools.reduce(operator.mul,lis)) 

# String Concat
print (functools.reduce(operator.add,["hello","world"])) 
