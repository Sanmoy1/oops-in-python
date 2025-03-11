#write a python program to remove the occurances of whitespace characters in a string
def remove_whitespace(s):
    return "".join(s.split(" "))
print(remove_whitespace("hello world"))
# print(" comeon ".join(["hello","world", "isthe"]))