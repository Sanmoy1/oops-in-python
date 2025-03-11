
def implement(s,sub):
    c=0
    a=s.split(" ")
    for i in a:
        if sub==i:
            c+=1
    return c


s=input("Enter the string: ")
sub=input("Enter the substring")
print("The number of occurances: ", implement(s,sub))