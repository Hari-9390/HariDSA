def binary_search(arr,target):
    left,right=0,len(arr)-1
    while left<=right:
        mid=(left+right)//2
        if arr[mid]==target:
            return mid
        elif arr[mid]< target:
            left=mid+1
        else:
            left=mid-1
    return -1
size=int(input("enter the size of the array"))
arr=[]
for num in range(size):
    num=int(input("ënter the element"))
    arr.append(num)
target=int(input("search the element"))
result=binary_search(arr,target)

if result != -1:
    print(f"Element found at index: {result}")
else:
    print("Element not found ")


