# Program to print most frequently occuring number in an array along with its frequency
from collections import Counter 
  
arr = [1, 3, 4, 1, 2, 1, 1, 3, 4, 3, 5, 1, 2, 5, 3, 4, 5] 
counter = Counter(arr) 
print(counter.most_common(3)) 
# returns [(key,frequency),(key,frequency)...] in descending order of frequency