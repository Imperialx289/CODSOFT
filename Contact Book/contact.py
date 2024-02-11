#!C:\Users\satyam\AppData\Local\Programs\Python\Python312\Python
print("Content-Type:text/html")
print()
import cgi

print("<h1>Data Enter Successfully</h1>")
print("<body bgcolor='gray'>")



form = cgi.FieldStorage()
Name = form.getvalue("Name")
EmailID = form.getvalue("EmailID")
PhoneNumber = form.getvalue("PhoneNumber")
Address = form.getvalue("Address")


import mysql.connector

con = mysql.connector.connect(host='localhost', user='root', database='lms')
cur = con.cursor()

i = "insert into codesoft values(%s,%s,%s,%s)"

t = (Name,EmailID,PhoneNumber,Address)

cur.execute(i, t)

con.commit()

cur.close()
