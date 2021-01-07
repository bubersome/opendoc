'''
Created on June 18, 2019
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
    conn.execute(table)                                 # could also create a cursor object


sql_insert = 'INSERT INTO names(name) VALUES(?)'        # table(column name)
one_name = ('Bill',)                                    # make sure to end with a comma

def insert_one(conn, sql=sql_insert, data=one_name):   
    conn.execute(sql, data)
    conn.commit()                                       # commit transaction
    
          
conn = connect()
insert_one(conn)
close(conn)









