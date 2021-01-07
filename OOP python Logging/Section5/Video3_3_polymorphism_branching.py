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
    def color(self):
        print('I am red')

class SomeOtherClass(PythonClass):
    def color(self):
        print('I am orange')

class NotFromPythonClass(object):
    def color(self):
        print('I am yellow')
        
        
a = PythonClass()
b = SomeClass()
c = SomeOtherClass()
d = NotFromPythonClass()

some_objects = [a, b, c, d]

for obj in some_objects:
    if isinstance(obj, PythonClass):
        obj.color()                         # if base or inherited class, we know it has the color() method
    else:
        print(type(obj))                    # Not in same class hierarchy, so we don't know...













  











