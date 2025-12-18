n=int(input("Enter size of array:"))
arr=[]
for i in range(n):
    arr.append(int(input(f"Enter element {i+1}: ")))
print("Arr: ",arr)
max=float('-inf')
min=float('inf')
for i in range(0,n):
    if arr[i]>max:
        min=max
        max=arr[i]
else:
        print("-1")

print(min) 