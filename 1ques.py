n=int(input("Enter the input of the array: "))
arr = []

for i in range(n):
    arr.append(int(input(f"Enter element {i+1}: ")))
print("Your array:", arr)
max=float("-inf")
min=float("inf")
for i in range(0,n):
    if arr[i]>max:
        min=max
        max=arr[i]
print(max,min)
