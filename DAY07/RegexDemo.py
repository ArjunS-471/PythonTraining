import re

pattern = '^a...s$'
test_string = 'abyss'
Result = re.match(pattern, test_string)

if Result:
    print("Succesful")
else:
    print("Search unsuccesful")