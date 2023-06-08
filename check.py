#!/usr/bin/python 
import sqlite3,cgi,cgitb
#David Martin
# COSC2P89
# 6995948
#dm20zo
# December 6th

form =cgi.FieldStorage() #Get the data from the Fields in the Front End

CreateUname= form.getvalue("user") # Create Username variable

CreatePassword= form.getvalue("pass") # Create Password Variable

print("Content-Type: text/html\n\n")

conn= sqlite3.connect("USERS.db") # Creates Database connection

#Function to Create Database

def CreateDatabase():

    conn.execute('''CREATE TABLE users(

        Username text UNIQUE,
        Password text

    );''') # Creates the SQL table

    conn.commit()
   

#Function in which Creates an account and stores the user into the Database 

def Createuser(Username,Password):

    c= conn.cursor()
    
    try:
        c.execute( "INSERT INTO users VALUES (?,?)",(Username,Password)) # Inserts the user into the data base

        conn.commit()

        print("You Have Created an Account !")

    except sqlite3.IntegrityError: # IF username already exists,  the user will not be entered into the data base

        print("Username Already exsits !")

        
    c.close()


    
Createuser(CreateUname,CreatePassword) # Calling the function


conn.close()


