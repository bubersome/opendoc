'''
Created on June 04, 2019
@author: Burkhard A. Meier




From the Python Standard Library documentation:
-----------------------------------------------
https://docs.python.org/3/library/pickle.html

"Warning: The pickle module is not secure against erroneous or 
maliciously constructed data. Never unpickle data received 
from an untrusted or unauthenticated source."

'''





import pickle


class PythonClass(object):
    def __init__(self, name='default name', items=None):      
        self.name = name 
        self.items = items
        print('*** init self.__dict__', self.__dict__)
        for item in self.items:   
            print(f'item in init: {item}')                 

    def get_name(self):
        for item in self.items:  
            print(f'item in get_name: {item}') 
        return self.name                
    
    # invoked during pickling
    def __getstate__(self): 
        print('self.__dict__ in __getstate__', self.__dict__)
        return self.__dict__.copy()
    
    # invoked during unpickling
    def __setstate__(self, state):
        print('\nself.__dict__ in __setstate__ before updating state ***')
        print(self.__dict__)
        self.__dict__.update(state)
        print('self.__dict__ in __setstate__ after updating state ***')
        print(self.__dict__)
        for item in self.items:  
            print(f'item in __setstate__: {item}') 

# create one instance of the PythonClass
some_items = [1, 2]
bob = PythonClass(name='Bob', items=some_items)
print('bob before:', bob.get_name())
print('\n*** before pickling ***')

# open a file in write binary mode and pickle the class object
with open('bob.pickle', 'wb') as bob_file:
    pickle.dump(bob, bob_file)

print('\n*** after pickling and before unpickling ***')

# open a file in read binary mode and unpickle the class object
with open('bob.pickle', 'rb') as unpickle_bob_file:
    bob_unpickled = pickle.load(unpickle_bob_file)

print('\n*** after unpickling ***')
print('bob after:', bob_unpickled.get_name())

















