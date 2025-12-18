n = int(input("Enter number of elements: "))
arr = []
for i in range(n):
    arr.append(int(input(f"Enter element {i+1}: ")))
print("Your array:", arr)
left=0
n=len(arr)
right=n-1
for i in range(len(arr)-1,-1,-1):
    while(left<right):
        arr[left],arr[right]=arr[right],arr[left]
        left+=1
        right-=1
print(arr)
    