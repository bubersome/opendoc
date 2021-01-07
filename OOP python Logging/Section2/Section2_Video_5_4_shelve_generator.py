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



db_shelf = shelve.open('PythonClassShelve.db')

data_dict_class_generator = (db_shelf[db_key] for db_key in db_shelf.keys())
print(data_dict_class_generator)

db_shelf.close()




