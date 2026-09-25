#Create a program to take in any user input and display an error message if any of the letters input are not a, b, c, d or e. 
# (If you want you can make it work for a single character first, then build from there)

noValid = 0
userInput = input("enter a message")

while noValid != len(userInput):
    for x in range(len(userInput)):
        if userInput[x] not in ("a","b","c","d","e"):
            print(userInput[x], "is not a vaild letter")
        else:
            noValid = noValid + 1
    if noValid != len(userInput):
        userInput = input("enter a message")
        noValid = 0