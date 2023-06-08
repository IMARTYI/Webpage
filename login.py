#!/usr/bin/python 

import cgi,sqlite3

#David Martin
# COSC2P89
# 6995948
#dm20zo
# December 6th

form =cgi.FieldStorage()

username= form.getvalue("user")

password=form.getvalue("pass")

print("Content-Type: text/html\n\n")
#print("test")
conn= sqlite3.connect("USERS.db")


def checkuser(user_,Pass_): # Function in which will check the database to check if the user exsits
    
    cursor= conn.cursor()

    cursor.execute('''SELECT * FROM users WHERE Username=:user_''',{'user_':user_}) # Grab hold of the record in Username where it is _user

    result = cursor.fetchone()

    if result is None:
        print("Wrong Credentials") # User not found
    elif result[1]== Pass_:

        print("You are Logged in") # User and password are correct
        
    else:

        print("Wrong Credentials") # Password is not complete 

checkuser(username,password) # Call the function

conn.close()