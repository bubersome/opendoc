'''
Created on Jun 18, 2019
@author: Burkhard A. Meier
'''



import shelve

        
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

data_dict_class.ID = 'ID_1'                  # assign a new attribute to the class instance


db_shelf = shelve.open('PythonClassShelve.db')

db_shelf[data_dict_class.ID] = data_dict_class  # store the entire class instance in the shelve database

db_shelf.close()




