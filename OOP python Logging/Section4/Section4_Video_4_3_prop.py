'''
Created on Jun 22, 2019
@author: Burkhard A. Meier
'''






class PythonSuperClass():
    def __init__(self, name, items):
        self._name = name
        self.items = items
    
    @property    
    def name(self):
        return self._name    
    
    @name.setter   
    def name(self, new_name):
        self._name = new_name        
        
    def get_name_and_items(self):   
        return self._name, self.items  
    
    
    def __repr__( self ):
        return f'PythonSuperClass({self._name}, {self.items})'    
    
        
class PythonClass(PythonSuperClass):
    def __init__(self, name, items=None):
        super().__init__(name, items)         

    def __str__(self):
        return "{name}, {items}".format(**self.__dict__)

    def __repr__( self ):
        return f'PythonClass({self.name}, {self.items})'


if __name__ == "__main__":  
    pythonclass = PythonClass(name="Oh, what a Name!")
    
    print(pythonclass._name)
    pythonclass.name  = "It is high Time for a change..."
    print(pythonclass._name)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



