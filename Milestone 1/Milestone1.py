import pandas as pd

#Defining function for counting words
def wordCounter(filename):
    fileHandle = open(filename,'r', encoding = 'UTF-8') #mentioning encoding as CSV was not in correct encoding
    wordDict = {}
    #looping through each line
    for line in fileHandle:
        #ignoring empty lines and new lines
        if line.strip() == '':
            continue
        else:
            line = line.strip()
            #spliting sentence with spaces to get words
            splitList = line.split()
            for word in splitList:
                if (word not in wordDict):
                    #adding new word to dictionary
                    wordDict[word] = 1
                else:
                    #update counter in dictionary
                    wordDict[word] += 1
    #Close file
    fileHandle.close()
    #Returning prepared dictionary
    return wordDict

filepath = r'C:\Users\Administrator\Desktop\UST_TRAINING\Milestone 1\Novel.csv'
wordCountDict = wordCounter(filepath)

#defining columns while converting to DataFrame
dfTable = pd.DataFrame(list(wordCountDict.items()), columns=['Word', 'Count'])
print(dfTable)