x=int(input("Enter value x: "))
y=int(input("Enter value y: "))
for i in range(x,y):
    count = 0
    for j in range(2,i):
        if(i%j==0):
            count+1=1 
    if(count == 0):
        print(i)
        
