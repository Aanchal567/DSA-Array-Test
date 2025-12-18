def moveZeroes(arr):
    n = len(arr)
    i = 0
    j = 0

    while j < n:
        if arr[j] == 0:
            j += 1       
        else:
            arr[i] = arr[j] 
            i += 1
            j += 1

    while i < n:
        arr[i] = 0
        i += 1
arr = [0, 1, 0, 3, 12]
moveZeroes(arr)
print(arr)