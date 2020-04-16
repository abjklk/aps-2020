# Isolating 1st set bit in a given number
# Step 1 : Take 2s Complement
# Step 2 : AND num with 2s complement 

n = 10
print(n&-n)