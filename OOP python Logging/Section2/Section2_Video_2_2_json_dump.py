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


# serialize the data to json format

twenty_nums = sample(range(100), 20)
with open('twenty_nums.json', 'w') as json_file:
    json.dump(twenty_nums, json_file, indent=2)


some_people =  {'people':
                    {'First': 'Bob', 
                     'Second': 'Bill', 
                     'Third': 'unknown'
                    }
                } 
with open('some_people.json', 'w') as json_file:
    json.dump(some_people, json_file, indent=2)







