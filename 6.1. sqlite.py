import sqlite3

## Connect to SQlite
connection=sqlite3.connect("student.db")

# Create a cursor object to insert record,create table
cursor=connection.cursor()

# create the table
table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT);
"""
# excute the table
cursor.execute(table_info)

# Insert Some more records
cursor.execute('''Insert Into STUDENT values('Danuja','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Usman','Information System Engineer','B',100)''')
cursor.execute('''Insert Into STUDENT values('Salitha','Data Science','A',86)''')
cursor.execute('''Insert Into STUDENT values('Anujitha','Cyber Security','A',50)''')
cursor.execute('''Insert Into STUDENT values('Radesh','Software Engineer','A',35)''')

# Disspaly ALl the records
print("The inserted records are")

# execute the qyery
data=cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)

# Commit your changes in the database     
connection.commit() 
  
# Closing the connection 
connection.close()