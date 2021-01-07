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
        print('*** init self.items', self.items)
        for item in self.items:   
            print(f'item in init: {item}')                 

    def get_name(self):
        for item in self.items:  
            print(f'item in get_name: {item}') 
        return self.name                


# create one instance of the PythonClass
some_items = [1, 2, 3]
bob = PythonClass(name='Bob', items=some_items)
print('bob before:', bob.get_name())
print('\nbefore pickling ***')

# open a file in write binary mode and pickle the class object
with open('bob.pickle', 'wb') as bob_file:
    pickle.dump(bob, bob_file)

print('after pickling and before unpickling ***')

# open a file in read binary mode and unpickle the class object
with open('bob.pickle', 'rb') as unpickle_bob_file:
    bob_unpickled = pickle.load(unpickle_bob_file)

print('\nafter unpickling ***')
print('bob after:', bob_unpickled.get_name())

















