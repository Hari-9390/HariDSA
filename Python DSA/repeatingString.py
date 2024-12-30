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

check_substring(main_string,sub_string)


def non_repeating_char(s):
    for char in s:
        if s.count(char)==1:
            return char
s=input("Enter string :")
res=non_repeating_char(s)

if res:
    print(f"The first non repeating character:{res}")
else:
    print("non repeating character found")'''


#Addition of two matrices

r=int(input("Enter no of rows:"))
c=int(input("Enter no of cols:"))
m1=[]
m2=[]

print("Enter elements into the m1 matrix")
for i in range(r):
    m1.append([int(input(f"Enter element m1[{i}{j}]:"))for j in range(c)])
print("Enter elements into the m2 matrix")
for i in range(r):
        m2.append([int(input(f"Enter element m2[{i}{j}]:"))for j in range(c)])
        result=[[m1[i][j]+m2[i][j]for j in range(c)] for i in range(r)]
print("Addition of matrix")
for row in result:
    print(row)
               



