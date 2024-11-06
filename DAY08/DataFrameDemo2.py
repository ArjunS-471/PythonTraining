import pandas as pd

data = {
    'Name' : ['A', 'B', 'C'],
    'Age' : [11,12,13],
    'Place' : ['BLR' , 'CHE', 'HYD']
}

# data = {
#     'Name' : 'A',
#     'Age' : 11,
#     'Place' : 'BLR'
# }

userInput = ""
while userInput != 3:
    print ("Choose a number from below - \n1. Add key value\n2. Display items in dictionary\n3. Exit")
    
    try:
        userChoice = int(input())

        if userChoice == 1:
            print("Mention Key")
            key = input()
            print("Mention value")
            value = input()
            data[key] = value.split(',')
        elif userChoice == 2:
            df = pd.DataFrame(data)
            print(df)
        elif userChoice == 3:
            print("Exiting app")
            break  
        else:
            print("Enter correct choice")
    
    except Exception as e:
        print("Error -", e,"\nEnter correct choice")
        print()

