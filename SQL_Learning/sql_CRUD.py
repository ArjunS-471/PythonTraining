import sqlite3

connection = sqlite3.connect(r'C:\Users\Administrator\Desktop\UST_TRAINING\SQL_Learning\Chinook_Sqlite.sqlite')
curr = connection.cursor()

print(curr)

# curr.execute("SELECT name from sqlite_master WHERE type = 'table';")

# tables = curr.fetchall()
# for table in tables:
#     print(table)

# curr.execute("SELECT * FROM 'Album' LIMIT 10;")
# data = curr.fetchall()

# for row in data:
#     print (row)

# desc = curr.description
# cols = [col[0] for col in desc]
# print(cols)

#CREATE operations
#CustomerId, FirstName, LastName, Company, Email, Country, Phone
# new_customer = (60,'Rajiv','RR', 'ABC','rajiv.rr@gmail.com', 'IND')

# curr.execute(
#     """
#     INSERT INTO Customer (CustomerId, FirstName, LastName, Company, Email, Country) VALUES (?,?,?,?,?,?)
#     """, new_customer
#              )

# connection.commit()
# print("New Customer Added")



# customer_company = 'UST'
# customer_id = 60
# new_email = 'sachin@ust.com'

# curr.execute(
#     """
#     UPDATE Customer SET Company = ?, Email = ? WHERE CustomerId = ?;
#     """, (customer_company, new_email, customer_id)
# )

# connection.commit()
# print("Customer updated")

curr.execute("DELETE FROM 'Customer' WHERE CustomerId = 60;")
connection.commit()

curr.execute("SELECT * FROM 'Customer' WHERE CustomerId = 60;")
data = curr.fetchall()
for row in data:
    print(row)

desc = curr.description
cols = [col[0] for col in desc]
print(cols)

