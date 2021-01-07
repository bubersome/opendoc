'''
Created on June 18, 2019
@author: Burkhard A. Meier
'''





import sqlite3

# triple quotes to span multiple lines
name_table = ''' CREATE TABLE IF NOT EXISTS names (         
                    id INTEGER PRIMARY KEY,
                    name text NOT NULL
                )'''

sql_insert = 'INSERT INTO names(name) VALUES(?)'        # table(column name)                           

many_names = [('Bob',),                                 # one-column table requires ending comma
              ('Sue',)
             ] 

sql_select = 'SELECT * FROM '               
                
                
class PythonClass(object):
    def __init__(self, db='PythonClass.db', table='names'):  
        self.db = db    
        self.table = table

    def connect(self):
        return sqlite3.connect(self.db)                                 # return connection object  
    
    def close(self, conn):
        conn.close()                                                    # close the connection                                  

    def create_table(self, conn):
        conn.execute(self.table)                                        # could also create a cursor object
    
    def insert_one(self, conn, sql=sql_insert, data=('Bill',)):   
        conn.execute(sql, data)
        conn.commit()                                                   # commit transaction
          
    def insert_many(self, conn, sql=sql_insert, data=many_names):   
        conn.executemany(sql, data)
        conn.commit()                                                   # commit transaction
    
    def select_all(self, conn, sql=sql_select):
        rows = conn.execute(sql + self.table)
        for row in rows:
            print(row)


if __name__ == '__main__':
    db_class = PythonClass()          
    conn = db_class.connect()
    db_class.select_all(conn)
    db_class.close(conn)









