def insertionSort(arr):    
    for i in range(1, len(arr)): 
        key = arr[i] 
        j = i-1
        while j >= 0 and key < arr[j] : 
            arr[j + 1] = arr[j] 
            j -= 1
        arr[j + 1] = key 
    return arr

a=[1,4,3,7,8,4]
print(insertionSort(a))
