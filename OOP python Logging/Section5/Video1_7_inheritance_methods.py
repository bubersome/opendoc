'''
Created on May 12, 2019
@author: Burkhard A. Meier
'''





#--------------------------------------------------
# Create class 'blue print'
#--------------------------------------------------

class BaseClass():
    
    def __init__(self, name='default'):         # BaseClass now has initializer with default arg
        self.name = name
    
    def print_base(self):
        print('Hello {} from BaseClass'.format(self.name))


class PythonClass(BaseClass):                   # inherit from BaseClass
    
    def __init__(self, a_name='Python'):             
        super().__init__(a_name)                # call initializer of Base (super) class, pass in arg

    
    def print_base(self):                           # create same-named method, overwriting base class method
        print('*** Hello from PythonClass ***')
        super().print_base()                        # call super() to invoke BaseClass method
        
                             
#--------------------------------------------------
# Create instance(s) of class
#--------------------------------------------------

instance = PythonClass()
instance.print_base()                   # call inherited method
























