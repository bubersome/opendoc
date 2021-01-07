'''
Created on June 05, 2019
@author: Burkhard A. Meier
'''






import json

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



#------------------------------------------------
# deserialize the data from json format
# 2. load from json into Python

with open('twenty_nums.json', 'r') as json_file:
    twenty_nums = json.load(json_file)

with open('some_people.json', 'r') as json_file:
    some_people = json.load(json_file)


data_list = PythonClass('data_list', twenty_nums)
print(data_list.get_name_items_dict())

no_data = PythonClass('no_data')
print(no_data.get_name_items_dict())

data_dict = PythonClass('data_dict', some_people)
print(data_dict.get_name_items_dict())

