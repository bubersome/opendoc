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


with open('some_people.yaml', 'w') as f:        # create some_people.yaml file
    yaml.dump(some_people, f)












