'''
Created on Jun 26, 2019
@author: Burkhard A. Meier
'''





class PythonSuperClass():
    def __init__(self, name, items):
        self.name = name
        self.items = items                  # can hold any type of data
        
    def get_name_and_items(self):   
        return self.name, self.items  
              
class PythonClass(PythonSuperClass):
    def __init__(self, name, items=None):
        super().__init__(name, items)         

if __name__ == "__main__":      
    name ="John"
    data = "John's Journal"
    data_class = PythonClass(name, data)                        # create regular class instance
    class_data = data_class.get_name_and_items() 
    print(class_data)
    print("Items:", type(class_data[1]))

 



