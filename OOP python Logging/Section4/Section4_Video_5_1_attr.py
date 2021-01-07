'''
Created on Jun 25, 2019
@author: Burkhard A. Meier
'''





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


if __name__ == "__main__":  
    
    name_of_class ="Oh, what a Name!"
    data_for_class = None

    data_dict_class = PythonClass(name_of_class, data_for_class) 
    class_data = data_dict_class.get_name_and_items() 

    print(class_data)
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 