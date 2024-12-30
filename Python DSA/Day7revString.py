def reverse(s):
    stack=[]
    for char in s:
        stack.append(char)
    reverse_string=""
    while stack:
        reverse_string+=stack.pop()
    return reverse_string
print(revv
