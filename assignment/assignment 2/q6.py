n=int(input("Enter the number: "))
c=0
for i in range(1,n):
    if n%i==0:
        c+=1
if c==1:
    print("prime number")
else:
    print("Not a prime number")