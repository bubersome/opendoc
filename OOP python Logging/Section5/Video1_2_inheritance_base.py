'''
Created on May 12, 2019
@author: Burkhard A. Meier
'''





#--------------------------------------------------
# Create class 'blue print'
#--------------------------------------------------

class BaseClass():
    
    def print_base(self):
        print('Hello from BaseClass')


class PythonClass(BaseClass):          # inherit from BaseClass
    
    def __init__(self):             
        pass

                     
#--------------------------------------------------
# Create instance(s) of class
#--------------------------------------------------

instance = PythonClass()
instance.print_base()                   # call inherited method
























