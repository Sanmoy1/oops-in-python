s=input("Enter the string: ")
upperCount=0
lowerCount=0
for i in s:
    
    if i.isupper():
        upperCount+=1
    else:
        lowerCount+=1
print("The count for uppercase: ",upperCount)
print("The count for the lowercase: ",lowerCount)