'''
Created on Jun 22, 2019
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
    people_set = set(['Bob', 'Bill', 'unknown', 'Bob', 'Bill', 'unknown'])      # set ignores dupes!
    
    data_dict_class = PythonClass('data_dict', people_set)
    class_data = data_dict_class.get_name_and_items() 
    print(type(class_data))

    for thing in class_data:
        if isinstance(thing, list):
            for _thing in thing:
                print("The Thing:", _thing)
        elif isinstance(thing, set):
            for _thing in thing:
                print("The Thing:", _thing)
        else:
            print("The Thing:", thing)

    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    