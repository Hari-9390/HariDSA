
def remove_consecutive_duplicates(string):
    stack=[]
    for char in string:
        if stack and stack[-1]==char:
            stack.pop()
        else:
            stack.append(char)
    result=""
    for char in stack:
        result+=char
    return result
print(remove_consecutive_duplicates("aabcddeeffa"))
