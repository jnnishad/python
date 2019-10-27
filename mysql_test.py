import mysql.connector


mydb = mysql.connector.connect(host="localhost",database='python_plugin',user="jai",passwd="jai@123")
mycursor = mydb.cursor()
mycursor.execute("select * from student;")
for i in mycursor:
    print(i)



