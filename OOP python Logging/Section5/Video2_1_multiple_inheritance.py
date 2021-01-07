'''
Created on May 17, 2019
@author: Burkhard A. Meier
'''





#--------------------------------------------------
# Create classes 
#--------------------------------------------------
class BaseClassTwo():
    def __init__(self, name='two'):         
        self.name = name
    
    def print_base(self):
        print('Hello {} from BaseClassTwo'.format(self.name))

#--------------------------------------------------
class BaseClass():
    def __init__(self, name='default'):         
        self.name = name
    
    def print_base(self):
        print('Hello {} from BaseClass'.format(self.name))

#--------------------------------------------------
class PythonClass(BaseClass, BaseClassTwo):         # inherit from BaseClass and BaseClassTwo
    def __init__(self, a_name='Python'):             
        super().__init__(a_name)                    # call initializer of Base (super) class, pass in arg

    
    def print_base(self):                           
        print('*** Hello from PythonClass ***')
        super().print_base()                        
                                    
#--------------------------------------------------
# Create instance(s) of class
#--------------------------------------------------
instance = PythonClass()
instance.print_base()                   # call inherited method
























