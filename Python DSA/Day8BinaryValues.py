
def generate_binary_numbers(n):
    queue=["1"]
    result=[]

    for i in range(n):
        current=queue.pop(0)
        result.append(current)
        queue.append(current+"0")
        queue.append(current+"1")
    return result
n=16
ot=generate_binary_numbers(n)
print(ot)






