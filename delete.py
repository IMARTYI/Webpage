#!/usr/bin/python 

import cgi,sqlite3

#   David Martin
#   COSC2P89
#   6995948
#   dm20zo
#   December 6th

form = cgi.FieldStorage()

deleteUsername= form.getvalue("user") # Grab the Username from the front end

deletePassword= form.getvalue("pass") # Grab the password from the front end

print("Content-Type: text/html\n\n")

conn = sqlite3.connect("USERS.db")

def deleteUser(_user,_pass): # Function to delete User

    cursor= conn.cursor()

    cursor.execute('''SELECT * FROM users WHERE Username=:_user''',{'_user':_user}) # Grab hold of the Accout

    account= cursor.fetchone() #Varaible use to check to seee if user is in database
    
    if account is None: # If user is not found in database
        print("User not Found")
    else:
        with conn:
            cursor.execute('''DELETE FROM users WHERE Username=:_user''',{'_user':_user}) # Delete the user if the user is found

        print("User is deleted")


deleteUser(deleteUsername,deletePassword) # Call Function

conn.close()
