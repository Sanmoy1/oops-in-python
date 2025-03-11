list =[[1,2,3],[1,2,3],[1,2,3]]
print(list)
print(len(list))
sum=0
for i in range(len(list)):
    for j in range(len(list[i])):
        if i==j:
            sum+=list[i][j]
print("The sum of the diagonals of the matrix: ",sum)