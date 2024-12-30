#Linear Search
def linear_search(arr,target):
    for i in range(len(arr)):
        if arr[i]==target:
            #print("Element found at index:",i)
            return i
    #else:
        #print("Element not found")
        return -1
size=int(input("Enter the size : "))
arr=[]

for num in range(size):
    num=int(input())
    arr.append(num)

target=int(input("Enter search element"))
result=linear_search(arr,target)
print(result)
    
if result!=-1:
    print("Element not found")
