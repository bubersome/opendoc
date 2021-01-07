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

def insert_one(conn, sql=sql_insert, data=('Bill',)):   
    conn.execute(sql, data)
    conn.commit()                                       # commit transaction
    

many_names = [('Bob',),                                 # one-column table requires ending comma
              ('Sue',)
             ] 
  
def insert_many(conn, sql=sql_insert, data=many_names):   
    conn.executemany(sql, data)
    conn.commit()                                       # commit transaction


sql_select = 'SELECT * FROM '
table = 'names'

def select_all(conn, sql=sql_select, table=table):
    rows = conn.execute(sql + table)
    for row in rows:
        print(row)

          
conn = connect()
select_all(conn)
close(conn)









