# Write a python program to read a sentence and display each word of the sentence taking the separator as punctuation marks.

def main():
    sentence = input("Enter a sentence: ")
    words = sentence.split(" ") 
    for word in words:
        print(word)
main()