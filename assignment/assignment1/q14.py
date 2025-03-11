s=input("Enter the string")
s.lower()
count=0
for i in s:
    if i=='a' or i=='e' or i=='o' or i=='u' or i=='i':
        count+=1
print("The number of vowels are: ", count)