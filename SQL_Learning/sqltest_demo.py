import sqlite3

connection = sqlite3.connect(r'C:\Users\Administrator\Desktop\UST_TRAINING\SQL_Learning\Chinook_Sqlite.sqlite')
curr = connection.cursor()

print(curr)

# curr.execute("SELECT name from sqlite_master WHERE type = 'table';")

# tables = curr.fetchall()
# for table in tables:
#     print(table)

curr.execute("SELECT * FROM 'Album' LIMIT 10;")
data = curr.fetchall()

for row in data:
    print (row)

desc = curr.description
cols = [col[0] for col in desc]
print(cols)