#Create a program to take in user input, but only allow the input if it contains the letters in your first name. 

noValid = 0
userInput = input("enter a message : ")

while noValid != len(userInput):
    for x in range(len(userInput)):
        if userInput[x] not in ('f','i','n','l','a','y'):
            print(userInput[x], "is not a vaild letter")
        else:
            noValid = noValid + 1
    if noValid != len(userInput):
        userInput = input("enter a message : ")
        noValid = 0