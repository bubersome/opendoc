'''
Created on Jun 20, 2019
@author: Burkhard A. Meier
'''







import argparse

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
    parser = argparse.ArgumentParser()
    parser.add_argument("class_name", help="Provide the name of a class to build",
                        choices=["PythonClass", "PythonSuperClass"])
    parser.add_argument("name", help="Building any of the classes requires a name")
    parser.add_argument("--items", help="Optionally add items to be added to the class")
    args_parsed = parser.parse_args()
    
    
