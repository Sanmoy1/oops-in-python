#write a python program to read first name and the last name of 5 person and display the name in correct format.

def main():
    name = []
    
    for i in range(5):
        n = input("Enter the first name and the last name: ")
        name.append(n)
        
    for i in name:
        first_name,last_name=i.split()
        

    