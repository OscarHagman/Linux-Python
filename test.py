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

def try_input_to_float():
    try_again = True
    num = 0
    while try_again:
        try:
            num = float(input())
            try_again = False
        except:
            print("You can only enter numbers, try again")
    return num

def try_input_operator():
    try_again = True    
    while try_again:
        op = input()
        if op == "+" or op == "-" or op == "*" or op == "/":
            try_again = False
            return op
        else:
            print("Invalid operator, try again")

is_run = True
while is_run:
    print("\n[1] Calculate" + "\n[2] Help" + "\n[3] Exit")

    menu_choise = input()
    if menu_choise == "1":
        print("\nEnter first digit")
        nr1 = try_input_to_float()

        print("Enter operator")
        operator = try_input_operator()
        
        print("Enter second digit")
        nr2 = try_input_to_float()
       
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

