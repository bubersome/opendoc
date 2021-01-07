'''
Created on May 17, 2019
@author: Burkhard A. Meier
'''





#--------------------------------------------------
# Polymorphism - with type checking
#--------------------------------------------------

class Logger(object):    
    def write_log(self, file_name=None, data=None):
        if not file_name:
            file_name = 'temp.txt'
        print(f'\nwriting to file: {file_name}')
        with open(file_name, 'w') as data_file:
            data_file.write(data)
            
class Database(Logger):
    def write_log(self, file=None):
        print('Opening database connection...')

class Networking(Logger):
    def write_log(self, file=None):
        print('Opening network socket...')

class Webserver(Logger):
    pass

class EmailServer(object):
    def write_log(self):
        print('Sending email...')
        

# Create objects        
a = Logger()
b = Database()
c = Networking()
d = Webserver()
e = EmailServer()

# Save objects instances/references in list
some_objects = [a, b, c, d, e]
data = 'This is data to be written to a file or elsewhere...'

# Loop through objects and call method, passing in data
for obj in some_objects:
    obj_type = type(obj)
    if isinstance(obj, Logger):
        try:
            obj.write_log(data=data)                 # if base or inherited class, we know it has the write_log() method
            print(obj_type, '\n')
        except Exception as ex:
            print('*** Exception:',obj_type, ex)
    else:
        print('Not in same class hierarchy:', obj_type)                          













  











