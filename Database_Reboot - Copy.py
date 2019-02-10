import sqlite3
import os
DRPASS = '1234'

print('-----Database Reboot------')
pas=input('Password : ')
if pas==DRPASS:
    print('Rebooting Database Will Delete existing Database...')
    ch=input('Do you wish to continue ? (Y) :')
    if ch=='Y':
        try:
             print('Deleting Existing Database...')
             os.remove("database.db")
             print('Database Deletion Successful!')
            
        except:
            pass
        print('Creating new Database...')
        conn = sqlite3.connect('database.db')
        print('Database Creation Successful!')

        print('Creating Tables...')

        conn.execute('''CREATE TABLE users
                 (name TEXT NOT NULL,
                 username TEXT PRIMARY KEY NOT NULL,
                 password TEXT NOT NULL,
                 mobilenum NUMBER NOT NULL);''')
        print('Created Users Table...') 

        conn.execute('''CREATE TABLE movies
                (movieid TEXT PRIMARY KEY NOT NULL,
                moviename TEXT NOT NULL,
                director TEXT NOT NULL,
                duration NUMBER NOT NULL);''')
        print('Created Menu Table...')

        conn.execute('''CREATE TABLE screen
                (screennum NUMBER PRIMARY KEY NOT NULL,
                floor NUMBER NOT NULL,
                capacity NUMBER NOT NULL,
                CHECK (capacity>0));''')
        print('Created Branch Table...')

        conn.execute('''CREATE TABLE shows
                (showid TEXT PRIMARY KEY NOT NULL,
                movieid TEXT NOT NULL,
                showtime DATETIME NOT NULL,
                screenno NUMBER NOT NULL,
                ava_seats NUMBER NOT NULL,
                CHECK (ava_seats>=0));''')
        print('Created Booking Table...') 

        conn.execute('''CREATE TABLE tickets
                (ticketid NUMBER PRIMARY KEY NOT NULL,
                username TEXT NOT NULL,
                showid TEXT NOT NULL,
                seats NUMBER NOT NULL);''')
        print('Created tables Table...')
        
        print('Table Creation Successful!') 

        conn.commit()
        conn.close()
    else:
        print('Exiting!')
else:
    print('Access Denied!')
os.system("pause")
