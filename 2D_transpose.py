# Program to transpose a 2D array

arr = [[1,2],[3,4],[5,6]]
print(list(zip(*arr)))  # [(1, 3, 5), (2, 4, 6)]