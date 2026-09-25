denary = int(input("Enter a number between -128 and -1"))

while denary < -128 or denary > -1:
    print("Try AGain")
    denary = int(input("Enter a number between -128 and -1"))

positive = abs(denary)

bitValues = [128, 64, 32, 16, 8, 4, 2, 1]
binary = ""

for bit in bitValues:
    if positive >= bit:
        binary += "1"
        positive -= bit
    else:
        binary += "0"

# Flip bits
flipped = ""

for bit in binary:
    if bit == "1":
        flipped += "0"
    else:
        flipped += "1"

# Add 1
binaryList = list(flipped)
carry = 1

for i in range(7, -1, -1):
    if carry == 1:
        if binaryList[i] == "0":
            binaryList[i] = "1"
            carry = 0
        else:
            binaryList[i] = "0"

result = "".join(binaryList)

print(result)

