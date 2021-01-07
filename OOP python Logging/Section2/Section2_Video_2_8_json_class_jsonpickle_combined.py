'''
Created on June 06, 2019
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
# deserialize class and data in json format

with open('some_people.json', 'r') as json_file:                    # load data
    some_people = json.load(json_file)                              # json.load

data_dict_class = PythonClass('data_dict', some_people)             # create class instance

with open('data_dict_class.json', 'w') as json_file:                # save class with data
    json_file.write(jsonpickle.encode(data_dict_class))             # jsonpickle.encode

with open('data_dict_class.json', 'r') as f:                        # deserialize class with data
    data_dict_class_decoded = jsonpickle.decode(f.read())           # jsonpickle.decode


print(data_dict_class_decoded.name)
print(data_dict_class_decoded.items)








