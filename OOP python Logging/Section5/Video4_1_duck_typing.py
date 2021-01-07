'''
Created on May 17, 2019
@author: Burkhard A. Meier
'''





#--------------------------------------------------
# Duck Typing - no type checking
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

class NotFromPythonClass(object):       # not in class hierarchy
    def color(self):
        print('I am yellow')

                   
a = PythonClass()
b = SomeClass()
c = SomeOtherClass()
d = NotFromPythonClass()

some_objects = [a, b, c, d]

for obj in some_objects:
    obj.color()                 # duck typing - see if it has the expected method                   



























  











