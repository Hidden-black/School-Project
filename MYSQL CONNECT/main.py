import mysql.connector
from mysql.connector import errorcode



cnx = mysql.connector.connect(user='root',password='mysql',
                              database='student',host='127.0.0.1' )


e = cnx.cursor()

#Run This when doing this for the first time
# e.execute("Create database student")
# e.execute("create table Student(name varchar(20),Rollno int,Class varchar(5),Sec varchar(3),Address varchar(20),City varchar(20),Pin int,Pc int)")
v=int(input("ENTER THE SERIAL NUMBER\n 1.Add Student\n 2.Show List\n"))

if v==1:
  a="Army Public School,Bolarum"
  b=input("Enter Student Name: ")
  c=int(input("Enter Student RollNo: "))
  d=input("Enter Student Class: ")
  f=input("Enter Student Section: ")
  g=input("Enter Student Address: ")
  h=input("Enter Student City: ")
  i=int(input("Enter Student Pin: "))
  j=int(input("Enter Student Contact: "))

  add_student = ("INSERT INTO Student "
                  "(name,Rollno,Class,Sec,Address,City,Pin,Pc)"
                  "VALUES (%s, %s, %s, %s, %s,%s, %s, %s)")

  studentdata= (f'{b}',c,f'{d}',f'{f}',f'{g}',f'{h}',i,j)
  e.execute(add_student,studentdata)
  cnx.commit()
elif v==2:
  a=int(input("Enter the student Rollno: "))
  query = ("SELECT * FROM Student WHERE Rollno = %s")
  e.execute(query,(a,))







cnx.close()