import pandas as pd
import sqlite3

connection = sqlite3.connect(r'C:\Users\Administrator\Desktop\UST_TRAINING\SQL_Learning\Chinook_Sqlite.sqlite')
curr = connection.cursor()

# query = """
# SELECT * FROM 'Customer' limit 10;
# """

#1. Determine the total sales for each country in the invoices table

query = """
SELECT BillingCountry, SUM(Total) AS TotalSales
FROM Invoice
GROUP BY BillingCountry;
"""

df_customers = pd.read_sql_query(query, connection)

# pandas code here
df_customers.groupby("BillingCountry")['Total'].sum().reset_index

print(df_customers)

# curr.execute("DELETE FROM 'Customer' WHERE CustomerId = 60;")
# connection.commit()

# curr.execute("SELECT * FROM 'Customer' WHERE CustomerId = 60;")
# data = curr.fetchall()
# for row in data:
#     print(row)

# desc = curr.description
# cols = [col[0] for col in desc]
# print(cols)

connection.close()