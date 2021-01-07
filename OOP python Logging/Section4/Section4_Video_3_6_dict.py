'''
Created on Jun 22, 2019
@author: Burkhard A. Meier
'''





class PythonSuperClass():
    def __init__(self, name, items):
        self.name = name
        self.items = items
        
    def get_name_and_items(self):   
        return self.name, self.items  
    
    def __repr__( self ):
        return f'PythonSuperClass({self.name}, {self.items})'    
    
        
class PythonClass(PythonSuperClass):
    def __init__(self, name, items=None):
        super().__init__(name, items)         

    def __str__(self):
        return "{name}, {items}".format(**self.__dict__)

    def __repr__( self ):
        return f'PythonClass({self.name}, {self.items})'


if __name__ == "__main__":  
    from pprint import pprint
    name_of_class = 'data_dict'
    
    dict_key_all = 'People, Cars & Airplanes'
    dict_1_key = 'people'
    dict_1_values = {'First': 'Bob', 
                     'Second': 'Bill', 
                     'Third': 'unknown'}
    
    dict_2_key = 'cars'
    dict_2_values =  {1: 'Ford', 
                      2: 'Tesla', 
                      3: 'Honda'}
    
    dict_3_key = 'airplanes'
    dict_3_values =  {'1': 'Boing', 
                      '2': 'Airbus', 
                      '3': 'Little Wing'}
    
    dict_all = {'People': {dict_1_key: dict_1_values},
                'Cars':   {dict_2_key: dict_2_values},
                'Planes': {dict_3_key: dict_3_values}
            }
      
    data_for_class = {dict_key_all: dict_all}
                          
    data_dict_class = PythonClass(name_of_class, data_for_class)
    class_data = data_dict_class.get_name_and_items() 

    pprint(class_data)









