'''
Created on June 17, 2019
@author: Burkhard A. Meier
'''





import sqlite3

def connect():
    return sqlite3.connect('PythonClass.db')        # return connection object  

def close(conn):
    conn.close()                                    # close the connection                                  

conn = connect()
print(conn)
close(conn)
print(conn)








