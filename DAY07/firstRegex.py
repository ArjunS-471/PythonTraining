# Capture all numbers in a string
import re

pattern = "\d*"
userString = input()

Result = re.findall(pattern, userString)

print(Result)