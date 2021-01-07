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


if __name__ == "__main__":      
    name ="Bill"
    data_list = [1, 3, 2]           
    data_list_class = PythonClass.from_list(name, data_list)    # use class name to call decorated method
    class_data = data_list_class.get_name_and_items() 
    print(class_data)
    print(type(class_data[1]))

 



