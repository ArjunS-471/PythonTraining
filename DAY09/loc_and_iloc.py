import pandas as pd

#student = pd.Series([50,55,60,65,70],index=list('ABCDE'))

#print(student)

#student.loc('C')

student_dictionary = {
    "RRR" : 100,
    "Mr. ABC" : 55,
    "Miss. M" : 75,
    "Mr. MNP" : 66
}

students=pd.Series(student_dictionary)
#print(students)
#print(students.iloc[2])
#print(students.loc['RRR'])

print(students[students > 80])