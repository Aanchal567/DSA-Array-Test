n = int(input("Enter your array size: "))
arr = []

for i in range(n):
    arr.append(int(input(f"Enter your element {i+1}: ")))

print(arr)

for i in range(0, n-1):
    if arr[i] < arr[i+1]:
        print("True!!")
    else:
        print("False!")
