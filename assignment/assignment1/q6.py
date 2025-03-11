n=int(input("Enter the number: "))
c=0
for i in range(2,n):
    for j in range(2,i):
        if(i%j==0):
            c+=1
    if c==0:
        print(i)
    c=0

