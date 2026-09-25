#Create a program to take in an ASCII character and display the appropriate 8-bit binary sequence.

character = (input("Please enter a character"))

while len(character) != 1:
    print("Must only be 1 character")
    character = (input("Please enter a character"))

# ord converts the character into an ACSII value
original = ord(character)

#format converts the ASCII chacter code into a 8 bit binary value
binary = format(original, "08b")

print(binary)