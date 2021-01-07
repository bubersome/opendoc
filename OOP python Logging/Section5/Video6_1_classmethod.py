'''
Created on May 17, 2019
@author: Burkhard A. Meier
'''




#--------------------------------------------------
# classmethod(s)
#--------------------------------------------------

class Colors():
    def __init__(self):
        self.colors = []
    
    @classmethod    
    def generate_data(cls):                                         # cls instead of self
        return ['blue', 'red', 'orange', 'yellow', 'black']
      
#--------------------------------------------------
class PythonClass(object):    
    def __init__(self, data=None):
        self.data = data                                            # data attribute
  
    @classmethod
    def create_data(cls, data_class):                               # cls = PythonClass
        data_list = []                                              # local list to hold data
        for data_item in data_class.generate_data():                # call classmethod of: Colors class 
            data_list.append(cls(data_item))                        # create instance of: PythonClass to hold data
        return data_list
#--------------------------------------------------

color_objects = PythonClass.create_data(Colors)                     # call classmethod of: PythonClass class
for obj in color_objects:
    print(obj.data)















