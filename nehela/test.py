# write a lamda function to calculate the square of a number and return the result
#write another py code for converting 1d array with 8 elements to 3d array with 2x2 elements

# Solution:
x= lambda a: a*a
print(x(5))

import numpy as np
arr = np.array([1,2,3,4,5,6,7,8])
newarr = arr.reshape(2,2,2)
print(newarr)