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

for k, v in class_data.items():
    if k == 'name':
        new_name = v
    elif k == 'items':
        new_some_people = v
            
new_data_dict_class = PythonClass(new_name, new_some_people)
new_class_data = new_data_dict_class.get_name_items_dict()
pprint(new_class_data)
print()


def write_csv():
    with open('PythonClass.csv', 'w') as csv_f:
        header_fields =['name','items','people','First','Second','Third']
        
        csv_writer = csv.DictWriter(csv_f, fieldnames=header_fields)    
        csv_writer.writeheader()
        csv_writer.writerow({'name': 'data_dict', 
                             'items': 'people',
                             'people': 'First',
                             'First': 'Bob',
                             'Second': 'Bill',
                             'Third': 'unknown'})
        
# write_csv()

def read_csv():
    with open('PythonClass.csv', 'r') as csv_f:
        csv_reader = csv.DictReader(csv_f)

        for row in csv_reader:
            return row

new_d = read_csv()   
python_d = {}
python_d['name'] = new_d['name']
python_d['items'] = {new_d['items']:{new_d['people']:new_d['First']}}
python_d['items']['people']['Second'] = new_d['Second']
python_d['items']['people']['Third'] = new_d['Third']
pprint(python_d)








