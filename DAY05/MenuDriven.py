userInput = ""
while userInput != 4:
    print ("Choose a number from below - \n1. Add numbers\n2. Subtract numbers\n3. Multiply numbers\n4. Exit")
    
    try:
        userChoice = int(input())

        if userChoice == 1:
            print("Input number 1")
            num1 = int(input())
            print("Input number 2")
            num2 = int(input())
            print("Sum =",num1 + num2)
        elif userChoice == 2:
            print("Input number 1")
            num1 = int(input())
            print("Input number 2")
            num2 = int(input())
            print("Difference =",num1 - num2)
        elif userChoice == 3:
            print("Input number 1")
            num1 = int(input())
            print("Input number 2")
            num2 = int(input())
            print("Product =",num1 * num2)
        elif userChoice == 4:
            print("Exiting app")
            break         
        else:
            print("Enter correct choice")
    
    except Exception as e:
        print("Error -", e,"\nEnter correct choice")
        print()

    