def print_results(filename, target_school):
    fileHandle = open(filename,'r')

    for line in fileHandle:
        line = line[:-1:]    #chop off newline at end
        print (1, line)
        splitList = line.split(',')
        college_name = splitList[1]

        if (college_name.strip == target_school.strip):
            print(line)
        else:
            print(college_name,target_school)
    
    fileHandle.close

filepath = r'C:\Users\Administrator\Desktop\UST_TRAINING\DAY08\File.csv'
target_word = 'UMass'

print_results(filepath, target_word)

