#Mark Carosella
#Project 04
#Data Structures

from arraystack import ArrayStack
from linkedstack import LinkedStack

continuePlaying = "Y"
while continuePlaying == "Y":
    strList = []
    poppedList = []
    comparisonIndex = 0
    userStr = input("Enter a string: ")
    userStr = userStr.lower() #Not case sensitive
    userStr = userStr.replace(" ","") #White spaces are irrelevant
    userStack = input("Type of stack (array or linked): ")
    for eachChar in userStr:
        strList.append(eachChar) #Create list of characters in string
   
    #Create the stack
    if userStack == "array":
        newStack = ArrayStack()
        for eachChar in userStr:
            newStack.add(eachChar)
    elif userStack == "linked":
        newStack = LinkedStack()
        for eachChar in userStr:
            newStack.add(eachChar)

    for eachChar in range(len(newStack) - 1):
        poppedChar = newStack.pop()
        poppedList.append(str(poppedChar)) #Create list of popped characters

    #Compare the str and popped lists, decide if palindrome
    for eachChar in strList:
        if eachChar != poppedList[comparisonIndex]:
            print("The string that you provided is not a palindrome.")
            break
        else:
            comparisonIndex += 1

        if comparisonIndex == (len(strList) - 1):
            print("The string that you provided is a palindrome.")
            break

    continuePlaying = input("Would you like to play again (Y or N)? ")

print("Thanks for playing!")
