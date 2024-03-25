#Input - Takes the numbers from the user, for the program to sort later.

symbols = ["`","~","!","@","$","%","^","&","*","(",")","_","+","=","/","{","}","|",":",",","<",">","?","'",'"',"[","]"," "]
numbers = ["1","2","3","4","4","5","6","7","8","9","0"]

#Symbolchecker - checks for symbols in an input
def symbol(word):
    for characters in word:
        if (characters in symbols)==True:
            return True
    return False

#Numberchecker - checks for numbers in an input
def number(word):
    for characters in word:
        if (characters in numbers)==True:
            return True
    return False

#Bubblesorter - Sorts numbers in numerical order based on the bubble sort algorithm
def bubbleSort(array):
    print("\nArray before sorting: "+str(array))
    l = len(array)
    for p in range(l):
        # Number of passes
        print("\nPass number: "+str(p+1))
        for j in range(0, l-p-1):
            #-9', '45', '-23', '0', '3'
        # size -p-1 because last p elements are already sorted in previous passes
            if float(array[j]) > float(array[j+1]) :
            # Swap element at jth position with (j+1)th position
                array[j], array[j+1] = array[j+1], array[j]
                print("\nArray after each pass: "+str(array))
            else:
                print("\nArray after each pass: "+str(array))
redo = True
numberArray = []
print("Number array at the beginning: "+str(numberArray))
while True:
    print("You will now be entering at least 2 numbers into the program, and the program will then sort these numbers for you in numerical order.")
    for i in range(2):
        digit = input("\nEnter a number: ")
        while symbol(digit)==True or any(i.isalpha() for i in digit)==True or number(digit)==True:
            if symbol(digit)==True:
                print("\nError, you entered a symbol which is an invalid input. Please only enter a number.")
                digit = input("Enter a number: ")
            if any(i.isalpha() for i in digit)==True:
                print("\nError, you entered a letter which is an invalid input. Please only enter a number.")
                digit = input("Enter a number: ")
            if number(digit)==True:
                numberArray.append(digit)
                print(numberArray)
                break
    while redo == True:
        digit = input("\nIf you would like the program to sort the numbers you have already entered, Enter 'n'.\nif you would like to continue using the program, enter another number : ")
        while symbol(digit)==True or any(i.isalpha() for i in digit)==True or number(digit)==True:
            if symbol(digit)==True:
                print("\nError, you entered a symbol which is an invalid input. Please only enter a number or 'n'.")
                digit = input("\nIf you would like the program to sort the numbers you have already entered, Enter 'n'.\nif you would like to continue using the program, enter another number : ")
            if any(i.isalpha() for i in digit)==True and digit!="n" and digit!="N":
                print("\nError, you entered a letter which is an invalid input. Please only enter a number or 'n'.")
                digit = input("\nIf you would like the program to sort the numbers you have already entered, Enter 'n'.\nif you would like to continue using the program, enter another number : ")
            if number(digit)==True:
                numberArray.append(digit)
                print(numberArray)
                break
            if digit=="n" or digit=="N":
                break
        if digit=="n" or digit=="N":
            redo = False    
    #Process - Sorts the inputted numbers using bubbleSort() function which was defined earlier
    bubbleSort(numberArray)

    #Output - Diplays the numbers after they are sorted
    print("\nThe sorted list is : ")
    for n in range(len(numberArray)):
        if n == len(numberArray)-1:
            print((numberArray[n]), end=".")
        else:
            print((numberArray[n]), end=", ")
    
    restart = (input("\n\nIf you would like to use this program again, please enter 'y' \nIf you would like to exit the program, please enter 'n': ")).lower()
    while restart!="y" and restart!="n":
        print("\nError, please enter one of the given options")
        restart = (input("If you would like to use this program again, please enter 'y' \nIf you would like to exit the program, please enter 'n': ")).lower()
    if restart=="n":
        break
    else:
        print("\nRestarting program\n")
        redo = True
