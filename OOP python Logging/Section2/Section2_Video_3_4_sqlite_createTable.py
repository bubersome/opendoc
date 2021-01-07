'''
Created on June 17, 2019
@author: Burkhard A. Meier
'''





import sqlite3

def connect():
    return sqlite3.connect('PythonClass.db')                # return connection object  

def close(conn):
    conn.close()                                            # close the connection                                  

# triple quotes to span multiple lines
name_table = ''' CREATE TABLE IF NOT EXISTS names (         
                    id INTEGER PRIMARY KEY,
                    name text NOT NULL
                )'''

def create_table(conn, table=name_table):
    conn.execute(table)                               # could also create a cursor object
         
conn = connect()
create_table(conn)
close(conn)









