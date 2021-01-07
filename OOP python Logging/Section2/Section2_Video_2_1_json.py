'''
Created on June 05, 2019
@author: Burkhard A. Meier
'''






import json
from random import sample

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


twenty_nums = sample(range(100), 20)
data_list = PythonClass('data_list', twenty_nums)

print(data_list.get_name())
print(data_list.get_items())
print(data_list.get_name_items_dict())
print()

no_data = PythonClass('no_data')
print(no_data.get_name_items_dict())
print()


some_people = {'First': 'Bob', 'Second': 'Bill', 'Third': 'unknown'}
data_dict = PythonClass('data_dict', some_people)
print(data_dict.get_items())
print(data_dict.get_name_items_dict())







