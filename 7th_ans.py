import mysql.connector
# import mysql.connector
#create user 'user'@'%' identified by 'password'
mydb = mysql.connector.connect(
  host="localhost",
  user="abc",
  password="password"
)
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("insert into Ruthik.ruthik_table values('Ruthik',1)")
mycursor.execute("insert into Ruthik.ruthik_table values('Ruthik',2)")
mydb.commit()
mycursor.execute("select * from Ruthik.ruthik_table")
for i in mycursor.fetchall():
    print(i)
mydb.close()