input_string = input("Enter the string: ")
char_frequency = {}


# Count frequency of each character
for i in input_string:
    if i in char_frequency:
        char_frequency[i] += 1
    else:
        char_frequency[i] = 1

# Print the frequency of each character
for char in char_frequency.items():
    print("The frequency of", char, ":")
