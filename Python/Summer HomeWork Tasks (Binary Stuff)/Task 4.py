#Create a program to take in a valid ordinal value and display the appropriate ASCII character.

number = int(input("Please enter a number between 0 and 127"))

while number < 0 or number > 127:
    print("invaild number")
    number = int(input("Please enter a number between 0 and 127"))

character = chr(number)

print(character)