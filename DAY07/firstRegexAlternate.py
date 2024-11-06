import re

def find_numbers_in_string(input_string):
    pattern = r'\d+'
    numbers = re.findall(pattern, input_string)
    return numbers

# input
input_string = 'There are 4 boxes, 5 pencils, 22 windows'
numbers = find_numbers_in_string(input_string)

print(numbers)