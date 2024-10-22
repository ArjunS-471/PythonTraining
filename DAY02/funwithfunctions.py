def say_hello(name):
    return "Hello " + name
#print(say_hello("Arjun"))


def thirdchar(name, n):
    return name[n-1:n]
#return name[n-1]

#print(thirdchar("Arjun",3))

def reverseString(name):
    return name[len(name)-1::-1]
#return name[::-1]

print(reverseString("Arjun"))