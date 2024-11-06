def print_results(filename):
    fileHandle = open(filename,'r')

    counts = {}

    for line in fileHandle:
        line = line[:-1:]    #chop off newline at end
        
        splitList = line.split(',')
        college_name = splitList[1]

        if college_name not in counts:
            counts[college_name] = 1
        else:
            counts[college_name] += 1
    print(counts)
    
    fileHandle.close

filepath = r'C:\Users\Administrator\Desktop\UST_TRAINING\DAY08\File.csv'

print_results(filepath)

