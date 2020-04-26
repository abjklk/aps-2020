# Program for finding lexicographic rank of string 
# Time Complexity : O(n)

import math

MAX_CHAR=256

count=[0]*(MAX_CHAR + 1)

def populateAndIncreaseCount(str): 
    for i in range(len(str)): 
        count[ord(str[i])]+=1

    for i in range(1,MAX_CHAR): 
        count[i] += count[i - 1]

def updatecount(ch): 
    for i in range(ord(ch),MAX_CHAR): 
        count[i]-=1

def findRank(str): 
    len1 = len(str)
    mul = math.factorial(len1)
    rank = 1
    populateAndIncreaseCount(str) 

    for i in range(len1): 
        mul = mul//(len1 - i)
        rank += count[ord(str[i]) - 1] * mul
        updatecount(str[i])
    return rank

str = "string"
print(findRank(str))

