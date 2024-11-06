#find words starting with specific letter

import re

#pattern = '^s[a-z]*'   #for 1st word
pattern = r'\b[s]\w*'   #for any number of words
test_string = 'sunday comes after saturday'

Result = re.findall(pattern, test_string)
print(Result)