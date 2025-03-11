# import numpy as np

# arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# print("\nOriginal 2D array:\n", arr_2d)

# # Slicing rows:
# print("\narr_2d[:2]:\n", arr_2d[:2])  # First two rows
# print("\narr_2d[1:]:\n", arr_2d[1:])   # From second row onwards

# # Slicing columns:
# print("\narr_2d[:, :2]:\n", arr_2d[:, :2])  # First two columns
# print("\narr_2d[:, 1:]:\n", arr_2d[:, 1:])   # From second column onwards

# # Slicing rows and columns together:
# print("\narr_2d[:2, :2]:\n", arr_2d[:2, :2])  # Top-left 2x2 sub-array
# print("\narr_2d[1:, 1:]:\n", arr_2d[1:, 1:])  # Bottom-right 2x2 sub-array

# # Accessing a single element:
# # Element at row index 1, column index 2 (value 6)
# print("\narr_2d[1, 2]:", arr_2d[1, 2])

# # Slicing creates a view (not a copy in most cases):
# slice_2d = arr_2d[:2, :2]
# slice_2d[0, 0] = 200  # Modifies the original array!
# print("Modified slice:\n", slice_2d)
# print("Original array after slice modification:\n", arr_2d)

import numpy as np

arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

print("Original array:\n", arr_2d)

print("\narr_2d[:, :2]:\n", arr_2d[:2])
print("\narr_2d[::2]:\n", arr_2d[::2])
