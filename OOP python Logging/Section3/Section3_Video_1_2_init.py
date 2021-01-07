'''
Created on Jun 19, 2019
@author: Burkhard A. Meier
'''








class PythonClassNoInit():
    pass
    
    
class PythonClass():   
    def __init__(self, name, items=None):
        self.name = name
        self.items = items
        
    def get_name_and_items(self):   
        return self.name, self.items            # returns a tuple 
    
    
PythonClass("This is my name")    
 


























