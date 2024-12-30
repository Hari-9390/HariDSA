'''#Selection_sort

def selection_sort(arr):
    n=len(arr)

    for i in range(n):
        min_index=i

        for j in range(i+1,n):
            if arr[j]<arr[min_index]:
                min_index=j
        arr[i],arr[min_index]=arr[min_index],arr[i]
size=int(input("Enter the size:"))
arr[]'''





#insertion sort

def insertion_sort(arr):
    for i in range(1,len(arr)):
        key=arr[i]

        j=i-1
        while j>=0 and key<arr[j]:
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=key
size=int(input("Enter the size:"))
arr[]


for i in range(size):
    num=int(input("Enter the element to add:"))
    arr.append(num)

result=insertion_sort(arr)

print("sorted array")
print(arr)








