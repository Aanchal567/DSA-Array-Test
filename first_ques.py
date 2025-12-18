def moveZeroes(arr):
    n = len(arr)
    i = 0  # position to place next non-zero element

    # Step 1: move all non-zero elements to the front
    for j in range(n):
        if arr[j] != 0:
            arr[i] = arr[j]
            i += 1

    # Step 2: fill the remaining positions with zero
    while i < n:
        arr[i] = 0
        i += 1

# Example usage
arr = [0, 1, 0, 3, 12]
moveZeroes(arr)
print(arr)   # Output: [1, 3, 12, 0, 0]
