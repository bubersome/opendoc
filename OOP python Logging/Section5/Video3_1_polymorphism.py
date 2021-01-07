'''
Created on May 17, 2019
@author: Burkhard A. Meier
'''





#--------------------------------------------------
# Polymorphism - with type checking
#--------------------------------------------------

class PythonClass(object):    
    def color(self):
        print('I am blue')

class SomeClass(PythonClass):
    def color(self):                # subclass overrides base class method
        print('I am red')

class SomeOtherClass(PythonClass):
    def color(self):                # subclass overrides base class method
        print('I am orange')


a = PythonClass()
b = SomeClass()
c = SomeOtherClass()

some_objects = [a, b, c]

for obj in some_objects:
    print(type(obj))                        # <class '__main__.PythonClass', SomeClass, SomeOtherClass>
    print(isinstance(obj, PythonClass))     # True for all three classes













  











