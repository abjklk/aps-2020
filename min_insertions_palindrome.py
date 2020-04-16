# Given a string what is the min. no of insertions required to make the string palindrome
# Step 1 : Take reverse of string
# Step 2 : Apply LCS on string,rev of string
# Step 3 : result = len(string) - len(lcs)
from lcs import lcs

s = "HELLO"
x = lcs(s,s[::-1])
print(len(s)-x)



