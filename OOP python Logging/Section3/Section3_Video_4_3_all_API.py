'''
Created on Jun 19, 2019
@author: Burkhard A. Meier
'''







__all__ = ['PythonClass']           # only what is define in __all__ can be imported


def can_import():
    print("I can be imported")

def _cannot_import():
    print("A leading _underscore should "+ 
          "prevent me from being imported")

class PythonSuperClass():
    def __init__(self, name, items):
        self.name = name
        self.items = items
        
    def get_name_and_items(self):   
        return self.name, self.items  
    
    def __repr__( self ):
        return f'PythonSuperClass({self.name}, {self.items})'
    
    
        
class PythonClass(PythonSuperClass):
    def __init__(self, name, items=None):
        super().__init__(name, items)         

    def __str__(self):
        return "{name}, {items}".format(**self.__dict__)

    def __repr__( self ):
        return f'PythonClass({self.name}, {self.items})'

 
    
 

















