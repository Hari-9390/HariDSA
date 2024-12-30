'''def linear_search(arr,target):
    for index in range(len(arr)):
        if(arr[index]==target):
            return index
    return -1
size=int(input("Enter the size:"))
arr=[]

for i in range(size):
    num=int(input("Enter the element to add:"))
    arr.append(num)

target=int(input("Enter the element you want to search:"))
result=linear_search(arr,target)

if result!=-1:
    print(f"Element found at index {result}")
else:
    print("Element not found")



#Binary Search

def binary_search(arr,target):
    left=0
    right=len(arr)-1

    while left<=right:
        mid=(left+right)//2
        if (arr[mid]==target):
            return mid
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1
    return-1
size=int(input("Enter the size:"))
arr=[]

for i in range(size):
    num=int(input("Enter the element to add:"))
    arr.append(num)

target=int(input("Enter the element you want to search:"))
result=binary_search(arr,target)

if result!=-1:
    print(f"Element found at index {result}")
else:
    print("Element not found")'''


#Bubble Sort

def bubble_sort(arr):
    n=len(arr)
    for i in range(0,n-1,1):
        for j in range(0,n-1,1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

size=int(input("Enter the size:"))
arr=[]

for i in range(size):
         num=int(input("Enter the element to add:"))
         arr.append(num)

result=bubble_sort(arr)

print("sorted array")
print(arr)






















