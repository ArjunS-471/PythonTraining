#create a function that return if the number is odd or even
def oddoreven (num):
    if num%2 == 1:
        print(num, "is an Odd number")
        return "ODD"
    else:
        print(num, "is an Even number")
        return "EVEN"

print ("Hello user, what is your number")
num_input = input()
#oddoreven(int(num_input))
print(oddoreven(int(num_input)))
