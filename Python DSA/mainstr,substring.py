'''s=input("enter the name")
dici={}
for i in s:
    if i not in dici:
        dici[i]=1
    else:
        dici[i]+=1
        print(dici)


def char_frequency(s):
    fre={}

    for char in s:
        if char in fre:
            fre[char]+=1
        else:
            fre[char]=1

    print("char frequency : ")
    for char,count in fre.items():
        print(f"{char}:{count}")
s=input("Enter a string ")
char_frequency(s)



def check_substring(main_string,sub_string):
    index=main_string.find(sub_string)
    if index !=-1:
        print(f"The substring starting at index : {index}")
    else:
        print("The substring not exist")

main_string=input("Enter the main string")
sub_string=input("Enter the substring")

check_substring(main_string,sub_string)'''


def non_repeating_char(s):
    for char in s:
        if s.count(char)==1:
            return char
s=input("Enter string :")
res=non_repeating_char(s)

if res:
    print(f"The first non repeating character:{res}")
else:
    print("non repeating character found")



