binary = []

number = int(input("Please enter number between 127 and -128"))

while number > 127 or number < -128:
    print("You dummy try again")
    number = int(input("Please enter number between 127 and -128"))

while number < -127 or number > 127:
    if number < 128:
        binary.append(0)
    elif number > 64:
        binary.append(1)
    elif number < 64:
        binary.append(0)
    elif number > 32:
        binary.append(1)
    elif number < 32:
        binary.append(0)
    elif number > 16:
        binary.append(1)
    elif number < 16:
        binary.append(0)
    elif number > 8:
        binary.append(1)
    elif number < 8:
        binary.append(0)
    elif number > 4:
        binary.append(1)
    elif number < 4:
        binary.append(0)
    elif number > 2:
        binary.append(1)
    elif number < 2:
        binary.append(0)
    elif number > 1:
        binary.append(1)
    elif number < 1:
        binary.append(0)

print(binary)