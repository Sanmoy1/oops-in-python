#write a program to read mobile number and display the number if it contains 10 digits. If not then display error message "mobile number must contain 10 digits".


mobile_number = input("Enter mobile number: ")

if len(mobile_number) == 10 and mobile_number.isdigit():
    
    mobile_list = [mobile_number]
    print(f"Mobile number: {mobile_number}")
else:
    print("Mobile number must contain 10 digits.")
