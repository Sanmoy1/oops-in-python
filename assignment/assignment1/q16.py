list=[1,2,2,3,4,5,6,7,7,7]
answer=[]
# c=0
for i in list:
    if i not in answer:
        answer.append(i)
print("The final list: ",answer)
