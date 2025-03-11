def rec(list):
    if not list:
        return 0
    else:
        return list[0]+rec(list[1:])

list=[1,2,3,4]
print("The sum of the list: ",rec(list))
