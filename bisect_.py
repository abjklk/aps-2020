# To get index of an element which is to be inserted in asorted array
import bisect

a = [1,2,4,7,9]
print(bisect.bisect(a,3))
# In case of same digits if to be inserted to left 
a = [1,2,3,4,7,9]
print(bisect.bisect_left(a,3))
# Right
print(bisect.bisect_right(a,3))
# if an element is to be inserted into the array
bisect.insort(a,0)
print(a)