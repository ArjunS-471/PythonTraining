
def invertDict(dict):
    returnDict = {}
    for key in dict:
        returnDict[dict[key]] = key
    

    #for key,value in dict.items():
        #returnDict[value] = key

    return returnDict

sample_dict = {1:'A', 2:'B', 3:'C'}
print(invertDict(sample_dict))