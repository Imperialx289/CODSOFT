#!C:\Users\satyam\AppData\Local\Programs\Python\Python312\Python
print("Content-Type:text/html")
print()

import cgi
import mysql.connector

# Establish database connection
try:
    con = mysql.connector.connect(host='localhost', user='root', database='lms')
    cur = con.cursor()
except mysql.connector.Error as err:
    print(f"<h2>Error connecting to the database: {err}</h2>")
    exit()

form = cgi.FieldStorage()
Name = form.getvalue("Name")
PhoneNumber = form.getvalue("PhoneNumber")
NewPhoneNumber = form.getvalue("NewPhoneNumber")
NewEmailID = form.getvalue("NewEmailID")

try:
    # Update contact details in the database
    update_query = "UPDATE codesoft SET PhoneNumber=%s, EmailID=%s WHERE Name=%s AND PhoneNumber=%s"
    cur.execute(update_query, (NewPhoneNumber, NewEmailID, Name, PhoneNumber))
    con.commit()
    
    # Check if any rows were affected
    if cur.rowcount > 0:
        print("<h2>Contact details updated successfully!</h2>")
    else:
        print("<h2>No contact details updated. Please check your input.</h2>")
except mysql.connector.Error as err:
    print(f"<h2>Error updating contact details: {err}</h2>")

cur.close()
con.close()
