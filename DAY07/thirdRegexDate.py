##capture any date in the format yyyy-mm-dd
import re

def find_date_in_string(input_string):
    #pattern = '[0-9]{4}-[0-9]{2}-[0-9]{2}'
    pattern = '\d{4}[-/]\d{2}[-/]\d{2}'
    #pattern = r'\b\d{4}-\d{2}-\d{2}'
    #pattern = r'\b\d{4}-\d{2}-\d{2}|\b\d{4}/\d{2}/\d{2}'
    numbers = re.findall(pattern, input_string,re.IGNORECASE)
    return numbers

# input
input_string = 'I have to work on 2024-02-02 and also on 2024/03/08'
numbers = find_date_in_string(input_string)

print(numbers)