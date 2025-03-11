a=int(input("Enter the 1st number: "))
b=int(input("Enter the 2nd number: "))
c=min(a,b)
gcd=1
for i in range(1,c+1):
    if a%i==0 and b%i==0:
        if i>gcd:
            gcd=i
print(f"The GCD for {a} and {b} is: ",gcd)