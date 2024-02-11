#!C:\Users\satyam\AppData\Local\Programs\Python\Python312\Python
print("Content-Type:text/html")
print()
import cgi
print("<body bgcolor='lightblue'>")
print("<link href='spot.css' rel='stylesheet'>")

import mysql.connector

con = mysql.connector.connect(host='localhost', user='root', database='lms')
cur = con.cursor()

form = cgi.FieldStorage()
Name = form.getvalue("Name")
PhoneNumber = form.getvalue("PhoneNumber")


# Fetch data based on the provided name and roll number
cur.execute("SELECT * FROM codesoft where Name=Name or PhoneNumber=PhoneNumber")
data = cur.fetchall()

cur.close()

print("<table border='1'>")
print("<tr><th>Name</th><th>PhoneNumber</th>")

if data:
    for row in data:
        print("<tr>")
        print("<td>{}</td>".format(row[0]))  
        print("<td>{}</td>".format(row[2]))  
        print("</tr>")
else:
    print("<tr>")
    print("<td colspan='3'>No matching data found. Please try again.</td>")
    print("</tr>")

print("</table>")
