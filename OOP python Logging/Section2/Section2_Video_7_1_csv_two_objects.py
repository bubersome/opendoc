'''
Created on Jun 18, 2019
@author: Burkhard A. Meier
'''




import csv
from pprint import pprint

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
class_data = data_dict_class.get_name_items_dict()
print(data_dict_class)
pprint(class_data)
print()

for k, v in class_data.items():
    if k == 'name':
        new_name = v
    elif k == 'items':
        new_some_people = v
            
new_data_dict_class = PythonClass(new_name, new_some_people)
new_class_data = new_data_dict_class.get_name_items_dict()
print(new_data_dict_class)
pprint(new_class_data)
print()






