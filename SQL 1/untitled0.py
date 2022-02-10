import sqlite3        
X=sqlite3.connect('test9.db')
Y=X.cursor()
print("new database created")
Y.execute('''Create table if not exists Company_2
             (ID int, Name text,Date_joined text,Place text,Salary integer,
              Age real);''')
print("A new table has been created") 
Y.execute('''insert into company_2 values
             (1,'Aaron','2001-1-12','India',150000,16 ),
             (2,'Shravan','2002-1-12','USA',170000,17),
             (3,'Colin','2003-1-12','Mananthavady',180000,18);''')

data=Y.execute("Select * from Company_2")
for k in data:
    print("ID=",k[0])
    print("Name=",k[1])
    print("Date_joined=",k[2])
    print("Place=",k[3])
    print("Salary=",k[4])
    print("Age=",k[5])
             
X.commit()
Y.close()             

