# Write a python program to read a sentence as well as a word. Display the number of occurrences of the word in the sentence. Also, read another word as input and use this word to replace the previous word in the input sentence and display it.

def main():
    sentence =input("Enter a sentence: ")
    word=input("enter a word:")
    replace_word=input("enter a word to replace")
    print("the frequenct of the chosen word is:",sentence.count(word))
    new_sentence=sentence.replace(word,replace_word)
    print("The new sentence with the replaced word is :",new_sentence)

main()