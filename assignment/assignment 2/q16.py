def comeon(n,power):
    if power==0:
        return 1
    else:
        return n*comeon(n,power-1)

n=int(input("Enter the number: "))
power=int(input("Enter the power: "))
print("The answer: ",comeon(n,power))
