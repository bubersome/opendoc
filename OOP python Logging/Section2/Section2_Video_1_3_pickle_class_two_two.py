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
    def __init__(self, name='default name'):      
        self.name = name                            

    def get_name(self):
        return self.name                

# create two instances of the PythonClass
bob = PythonClass(name='Bob')
print('bob before:', bob.get_name())


bill = PythonClass(name='Bill')
print('bill before:', bill.get_name())


# open a file in write binary mode and pickle the class object
with open('two.pickle', 'wb') as two_file:
    pickle.dump(bob, two_file)
    pickle.dump(bill, two_file)
 
# open a file in read binary mode and unpickle the class object
with open('two.pickle', 'rb') as unpickle_two_file:
    two_unpickled = pickle.load(unpickle_two_file)
    second_two_unpickled = pickle.load(unpickle_two_file)
 
print('bob after:', two_unpickled.get_name())
print('bill after:', second_two_unpickled.get_name())




# bob before: Bob
# bill before: Bill
# bob after: Bob
# bill after: Bill











