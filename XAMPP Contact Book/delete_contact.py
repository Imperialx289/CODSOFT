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

try:
    # Delete contact from the database
    delete_query = "DELETE FROM codesoft WHERE Name=%s AND PhoneNumber=%s"
    cur.execute(delete_query, (Name, PhoneNumber))
    con.commit()
    
    # Check if any rows were affected
    if cur.rowcount > 0:
        print("<h2>Contact deleted successfully!</h2>")
    else:
        print("<h2>No contact deleted. Please check your input.</h2>")
except mysql.connector.Error as err:
    print(f"<h2>Error deleting contact: {err}</h2>")

cur.close()
con.close()
