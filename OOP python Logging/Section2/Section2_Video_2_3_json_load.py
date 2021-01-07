'''
Created on June 05, 2019
@author: Burkhard A. Meier
'''






import json
from random import sample   # <-- no longer used

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


# deserialize the data from json format
# 1. simply read the files

with open('twenty_nums.json', 'r') as json_file:
    twenty_nums_json = json_file.read()

with open('some_people.json', 'r') as json_file:
    some_people_json = json_file.read()

print(twenty_nums_json)
print(some_people_json)

print(type(twenty_nums_json))
print(type(some_people_json))

#------------------------------------------------
# deserialize the data from json format
# 2. load from json into Python

with open('twenty_nums.json', 'r') as json_file:
    twenty_nums = json.load(json_file)

with open('some_people.json', 'r') as json_file:
    some_people = json.load(json_file)

print('\nfrom json.load -----------------------------------------------------------------\n')

print(twenty_nums)
print(some_people)

print(type(twenty_nums))
print(type(some_people))

