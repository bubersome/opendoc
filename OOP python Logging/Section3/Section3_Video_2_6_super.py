'''
Created on Jun 19, 2019
@author: Burkhard A. Meier
'''







class PythonSuperClass():
    def __init__(self, name, items):
        self.name = name
        self.items = items
        
    def get_name_and_items(self):   
        return self.name, self.items  
    
    
class PythonClass(PythonSuperClass):
    def __init__(self, name, items=None):
        super().__init__(name, items)
            
      
bob = PythonClass(name="Bob", items=[42, 'Spaceship']) 
print(bob.get_name_and_items())

















