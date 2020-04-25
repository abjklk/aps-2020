import itertools 

# accumulate() returns a iterator containing the intermediate results.
lis = [1,6,3,5,2,5] 

# Sort of cumulative 
# Accumulate sum 
print (list(itertools.accumulate(lis,lambda x,y : x+y)))