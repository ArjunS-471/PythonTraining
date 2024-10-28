def removevowels(str):
    output = ""
    for i in str:
        if i not in ['a','e','i','o','u']:
             output += i
    return output

print(removevowels("arjun"))