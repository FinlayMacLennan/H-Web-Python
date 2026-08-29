#Create a program to take in a valid denary number between 0 and 255, and display the appropriate 8-bit binary sequence.

denary = int(input("Enter a number between 0 and 255"))

while denary < 0 or denary > 255:
    print("try AGain")
    denary = int(input("Enter a number between 0 and 255"))

bitValues = [128, 64, 32, 16, 8, 4, 2, 1]
binary = ""

for bit in bitValues:
    if denary >= bit:
        binary += "1"
        denary -= bit
    else:
        binary += "0"

print(binary)