'''
Created on Jun 26, 2019
@author: Burkhard A. Meier
'''





class PythonSuperClass():
    def __init__(self, name, items):
        self.name = name
        self.items = items                  # can hold any type of data
        
    def get_name_and_items(self):   
        return self.name, self.items  
              
class PythonClass(PythonSuperClass):
    def __init__(self, name, items=None):
        super().__init__(name, items)         

    @classmethod                            # decorator
    def from_list(cls, name, items):
        if not isinstance(items, list):     # expect a list
            items = []                      # create empty list      
        return cls(name, items)             # create and return instance

    @classmethod
    def from_dict(cls, name, items):
        if not isinstance(items, dict):     # expect a dict
            items = {}                      # create empty dict      
        return cls(name, items)             # create and return instance

    @staticmethod
    def static_set():
        return PythonClass(name='Static', items={0, 100})   # default values, return class instance

if __name__ == "__main__":      
    data_static = PythonClass.static_set()               # use class name and static method with default values
    class_data = data_static.get_name_and_items() 
    print(class_data)
    print(type(class_data[1]))

 



