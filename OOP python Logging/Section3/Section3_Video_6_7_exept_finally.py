'''
Created on Jun 20, 2019
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
    try:
        bob = PythonClass("Bob") 
        print(bob.get_name_and_items())
        try:          
            PythonSuperClass("Space")
            print('It worked!')
        except:
            pass    
        
        PythonSuperClass.a_new_attribute = 'A new attribute'
        
        walker = PythonSuperClass("Space", 1)
        print(walker)
        
        print(walker.a_new_attribute)       
        walker.a_new_attribute = None
        
        print(walker.a_new_attribute)
        
    except Exception as ex:
        print('caught:', str(ex))

    finally:
        del PythonSuperClass.a_new_attribute
        print('finally after deleting new attr')
        

        
 


























