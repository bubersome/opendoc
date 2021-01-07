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

class NotFromPythonClass(object):           
    def color(self):
        print('I am yellow')

class NotFromPythonClassNoMethod(object):
    def color_1(self):                          # different method name
        print('I am black')
                
        
a = PythonClass()
b = SomeClass()
c = SomeOtherClass()
d = NotFromPythonClass()
e = NotFromPythonClassNoMethod()

some_objects = [a, b, c, d, e, a]

for obj in some_objects:
    if hasattr(obj, 'color'):
        obj.color()                                   
    else:
        print(f'Object {obj} does not have the required attribute')


























  











