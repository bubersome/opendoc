'''
Created on May 17, 2019
@author: Burkhard A. Meier
'''




#--------------------------------------------------
# classmethod(s)
#--------------------------------------------------
from random import randint

class DataClass():
    def __init__(self):
        self.data = []
    
    @classmethod    
    def generate_data(self):
        raise NotImplementedError

#--------------------------------------------------        
class Colors(DataClass):
    def __init__(self):
        super().__init__()
    
    @classmethod    
    def generate_data(cls):
        return ['blue', 'red', 'orange', 'yellow', 'black']

#--------------------------------------------------        
class Numbers(DataClass):
    def __init__(self):
        super().__init__()
    
    @classmethod    
    def generate_data(cls):
        return [randint(0, 100) for _ in range(5)]
      
#--------------------------------------------------
class PythonClass(object):    
    def __init__(self, data=None):
        self.data = data                                            # data attribute
  
    @classmethod
    def create_data(cls, data_class):                               # pass in class name of: PythonClass
        data_instance = data_class()                                # create instance of: Colors to hold data
        for data_item in data_class.generate_data():                # call classmethod of: Colors class 
            data_instance.data.append(cls(data_item))               # create instance of: PythonClass to hold data
        return data_instance.data
#--------------------------------------------------

stars = '*' * 10
color_objects = PythonClass.create_data(Colors)
print('\nColors:\n' + stars)
for obj in color_objects:
    print(obj.data)

number_objects = PythonClass.create_data(Numbers)
print('\nNumbers:\n' + stars)
for obj in number_objects:
    print(obj.data)









