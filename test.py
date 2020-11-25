def getSum (num1, num2):
    return num1 + num2

def getDif (num1, num2):
    return num1 - num2

def getPro (num1, num2):
    return num1 * num2

def getQuo (num1, num2):
    return num1 / num2

def spotOn (sum):
    if sum < 50 and sum > 1:
         print("Less then fifty")
    elif sum == 50:
         print("Fifty")
    elif sum > 50 and sum < 100:
         print("Almost a hundred")
    elif sum == 100:
         print("Spot on!")
    elif sum > 100:
         print("Missed the spot!")
    else:
        print("Less than 1!")



is_run = True
while is_run:
    print("\n[1] Calculate" + "\n[2] Help" + "\n[3] Exit")

    menu_choise = input()
    if menu_choise == "1":
        nr1 = float(input("\nEnter first digit: "))
        operator = input("Enter operator: ")
        nr2 = float(input("Enter second digit: "))
       
        if operator == "+":
            print(str(nr1) + " + " + str(nr2) + " = " + str(getSum(nr1, nr2)))
            spotOn(getSum(nr1, nr2))

        elif operator == "-":
            print(str(nr1) + " - " + str(nr2) + " = " + str(getDif(nr1, nr2)))
            spotOn(getDif(nr1, nr2))

        elif operator == "*":
            print(str(nr1) + " * " + str(nr2) + " = " + str(getPro(nr1, nr2)))
            spotOn(getPro(nr1, nr2))

        elif operator == "/":
            print(str(nr1) + " / " + str(nr2) + " = " + str(getQuo(nr1, nr2)))
            spotOn(getQuo(nr1, nr2))

        else:
            print("\nSomething went wrong, try again")
        

    elif menu_choise == "2":
        print("\nWELCOME TO MY CALCULATOR APP!\n\nTo use this simple calculator, " + 
        "simply press '1' in the main menu,\nenter the number you want to calculate, " + 
        "enter what operator you would like to use. ('+' '-' '*' '/')" +
        "\nAnd lastly, enter the second number, then the program will do the calculation!")
   
    elif menu_choise == "3":
        print("\nExiting, good bye...\n")
        is_run = False
    
    else:
        print("\nYou can only choose between 1 and 3 in this menu")

