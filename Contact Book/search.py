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

# Input validation
if not Name and not PhoneNumber:
    print("<p>Please provide either a name or a phone number to search.</p>")
else:
    # Construct the SQL query
    query = "SELECT Name, PhoneNumber FROM codesoft WHERE Name LIKE %s OR PhoneNumber LIKE %s"
    # Execute the query with placeholder values
    cur.execute(query, ('%' + Name + '%', '%' + PhoneNumber + '%'))
    data = cur.fetchall()

    cur.close()

    print("<table border='1'>")
    print("<tr><th>Name</th><th>PhoneNumber</th></tr>")

    if data:
        for row in data:
            print("<tr>")
            print("<td>{}</td>".format(row[0]))  
            print("<td>{}</td>".format(row[1]))  
            print("</tr>")
    else:
        print("<tr>")
        print("<td colspan='2'>No matching data found. Please try again.</td>")
        print("</tr>")

    print("</table>")
