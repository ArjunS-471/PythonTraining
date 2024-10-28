userInput = ""
while userInput != 4:
    print ("Choose a number from below - \n1. Add numbers\n2. Subtract numbers\n3. Multiply numbers\n4. Exit")
    
    try:
        userChoice = int(input())

        if userChoice == 4:
            print("Exiting app")
            break
        elif userChoice in [1, 2, 3, 4]:
            print("Input number 1")
            num1 = int(input())
            print("Input number 2")
            num2 = int(input())

            if userChoice == 1:
                print("Sum =",num1 + num2)
            elif userChoice == 2:
                print("Difference =",num1 - num2)
            elif userChoice == 3:
                print("Product =",num1 * num2)
            else:
                print("Exiting app")
                break         
        else:
            print("Incorrect choice, enter correct choice\n")
    
    except Exception as e:
        print("Error -", e,"\nEnter correct choice")
        print()

    