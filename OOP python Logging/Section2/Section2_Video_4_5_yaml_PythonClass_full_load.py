'''
Created on Jun 18, 2019
@author: Burkhard A. Meier
'''




import yaml

class PythonClass(object):
    def __init__(self, name='default name', items=None):      
        self.name = name    
        self.items = items                        

    def get_name(self):
        return f"Name is: {self.name}"                

    def get_items(self):
        return f"Items are: {self.items}"
            
    def get_name_items_dict(self):
        return dict(name = self.name,
                    items = self.items)
        
        
some_people = {'people': {'First': 'Bob', 'Second': 'Bill', 'Third': 'unknown'}}

data_dict_class = PythonClass('data_dict', some_people)
print(data_dict_class)
 
 
with open('data_dict_class.yaml', 'r') as f:                        # deserialize class with data
    data_dict_class_loaded = yaml.full_load(f) 
print(data_dict_class_loaded)
print(data_dict_class_loaded.get_name_items_dict())                 # call method




