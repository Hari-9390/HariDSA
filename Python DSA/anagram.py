'''def anagrams(str1,str2):
    str1=str1.replace(" ","").lower()
    str2=str2.replace(" ","").lower()
    return sorted(str1)==sorted(str2)
str1=input()
str2=input()
if anagrams (str1,str2):
    print("strings are anagram")
else:
    print("strings are not anagram")'''



def duplicate_characters(s):
    result=""
    for char in s:
        if char not in result:
            result += char
    return result
str1=input("Enter the string ")
res=duplicate_characters(str1)
print("modified string",res)
