# Program to sort list of lists based on nth index in the sublists

a = [[1,3],[2,10],[87,1],[27,99],[63,8]]

# to sort the list according to column 2 :
a.sort(key = lambda x : x[1])
print(a)

#default fn sorts based on first column
a.sort() 
print(a)
