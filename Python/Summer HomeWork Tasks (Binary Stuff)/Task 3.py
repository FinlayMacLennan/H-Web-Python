#Create a program to take in an ASCII character and display its ordinal value.

character = (input("Please enter a character"))

while len(character) != 1:
    print("Must only be 1 character")
    character = (input("Please enter a character"))

original = ord(character)
print(original)