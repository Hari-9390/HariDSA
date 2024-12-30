#quick sort

def quick_sort(arr):
    if len(arr)<=1:
        return arr

    pivot=arr[len(arr)//2]

    left=[x for x in arr if x<pivot]
    middle=[x for x in arr if x==pivot]
    right=[x for x in arr if x>pivot]

    return quick_sort(left)+middle+quick_sort(right)


size=int(input("Enter the size:"))
arr=[]

for i in range(size):
         num=int(input(f"Element {i+1}:"))
         arr.append(num)

result=quick_sort(arr)

print("sorted array")
print(result)

    
