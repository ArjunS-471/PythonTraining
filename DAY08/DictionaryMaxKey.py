

def MaxDictionry (dict):
    MaxDict = {}
    MaxDict = dict

    temp = 0

    for key in dict:
        if key > temp:
            temp = key
    return temp

userDict = {10:0, 1:2, 2:3, 3:4, 4:5}

print(MaxDictionry(userDict))
print(Max(userDict.keys))