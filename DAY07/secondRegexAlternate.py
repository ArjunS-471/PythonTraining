import re

def find_charWord_in_string(input_string):
    pattern = r'[s][a-z]*'
    #pattern = r'\bs\w*'
    numbers = re.findall(pattern, input_string,re.IGNORECASE)
    return numbers

# input
input_string = 'She sells sea shells by the sea shore'
numbers = find_charWord_in_string(input_string)

print(numbers)