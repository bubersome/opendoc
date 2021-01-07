'''
Created on May 17, 2019
@author: Burkhard A. Meier
'''





#--------------------------------------------------
# Create classes 
#--------------------------------------------------
class BaseClassTwo():
    def __init__(self, name='two'):   
#         self.name = name                            # bug! using same name as in BaseClass     
        self.name_two = name                      # choose a different variable name
        print('I am BaseClassTwo')                  # runs when BaseClassTwo gets created
    
    def print_base(self):
        print('Hello {} from BaseClassTwo'.format(self.name_two))

#--------------------------------------------------
class BaseClass():
    def __init__(self, name='default'):         
        self.name = name
        print('I am BaseClass')                     # runs when BaseClass gets created
    
    def print_base(self):
        print('Hello {} from BaseClass'.format(self.name))

#--------------------------------------------------
class PythonClass(BaseClass, BaseClassTwo):             # inherit from BaseClass and BaseClassTwo
    def __init__(self, a_name='Python', two='2'):             
        super().__init__(a_name)                        # call initializer of Base (super) class, pass in arg
        BaseClassTwo.__init__(self, two)                # call initializer of Second Base class using class name
                                                        # no parenthesis, and passing in self into init!
    
    def print_base(self):                           
        print('*** Hello from PythonClass ***')
        super().print_base()         
        BaseClassTwo.print_base()          
                                    
#--------------------------------------------------
# Create instance(s) of class
#--------------------------------------------------
instance = PythonClass()
instance.print_base()                   # call inherited method
























