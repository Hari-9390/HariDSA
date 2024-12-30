def duplicate_characters(s):
    result=""
    for char in s:
        if char not in result:
            result += char
    return result
str1=input("Enter the string ")
res=duplicate_characters(str1)
print("modified string",res)
