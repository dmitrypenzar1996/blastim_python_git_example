#!/usr/bin/python3

first_name = input("Input your first name: ")
last_name = input("Input your last name: ")
option = int(input("Should I say hello (inuput 1) or goodbye (input 2)?"))

if option == 1:
    print(f"Hello, {first_name} {last_name}") 
elif option == 2:   
    print(f"Goodbye, {first_name} {last_name}") 
else:
    raise Exception("Wrong option")

