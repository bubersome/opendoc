'''
Created on Jun 19, 2019
@author: Burkhard A. Meier
'''







class PythonSuperClass():
    def __init__(self):
        pass


class PythonClass(PythonSuperClass):
    def __init__(self, name, items=None):
        super().__init__()
    
        self.name = name
        self.items = items
        
    def get_name_and_items(self):   
        return self.name, self.items  

        
PythonClass(name="Bob") 

















