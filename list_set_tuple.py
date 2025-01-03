#this is the program to get to know all list, set and tuple 
# Demonstrating the differences between List, Tuple, and Set in Python

# 1. List: Mutable, ordered, allows duplicates
my_list = [1, 2, 3, 4, 4, 5]
print("List:", my_list)

# Modifying a list
my_list[0] = 10
print("Modified List:", my_list)

# Allows duplicates
my_list.append(4)
print("List with duplicates:", my_list)


# 2. Tuple: Immutable, ordered, allows duplicates
my_tuple = (1, 2, 3, 4, 4, 5)
print("\nTuple:", my_tuple)

# Accessing elements
print("Accessing first element of tuple:", my_tuple[0])

# Tuples are immutable
try:
    my_tuple[0] = 10
except TypeError as e:
    print("Error modifying tuple:", e)

# 3. Set: Mutable, unordered, does not allow duplicates
my_set = {1, 2, 3, 4, 4, 5}  # Duplicate values will be removed
print("\nSet:", my_set)

# Modifying a set
my_set.add(6)
print("Set after adding an element:", my_set)

# Sets do not allow duplicates
my_set.add(4)
print("Set after attempting to add a duplicate:", my_set)

# Summary
print("\nSummary:")
print("List: Mutable, Ordered, Allows duplicates")
print("Tuple: Immutable, Ordered, Allows duplicates")
print("Set: Mutable, Unordered, Does not allow duplicates")
