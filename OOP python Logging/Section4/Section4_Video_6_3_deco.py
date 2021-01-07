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

if __name__ == "__main__":      
    name ="Bob"
    data_dict = {'One': 1,'Three': 3}           
    data_dict_class = PythonClass.from_dict(name, data_dict)    # use class name to call decorated method
    class_data = data_dict_class.get_name_and_items() 
    print(class_data)
    print(type(class_data[1]))

 



