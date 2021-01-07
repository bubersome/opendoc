'''
Created on June 05, 2019
@author: Burkhard A. Meier
'''






import json
import jsonpickle

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
# try to serialize class in json format

python_class = PythonClass()
print(python_class)

# with open('PythonClass.json', 'w') as json_file:
#     json.dump(python_class, json_file)            # TypeError: Object of type PythonClass is not JSON serializable

with open('PythonClass.json', 'w') as json_file:
    json_file.write(jsonpickle.encode(python_class))




