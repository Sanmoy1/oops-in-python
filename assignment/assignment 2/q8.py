string=input("Enter the string: ")
substring=input("Enter the substring: ")
split=string.split(" ")
count=0
for i in split:
    if substring==i:
        count+=1
print("The number of occurance of a substring: ",count)
