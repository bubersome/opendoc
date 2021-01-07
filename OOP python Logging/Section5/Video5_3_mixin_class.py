'''
Created on May 17, 2019
@author: Burkhard A. Meier
'''





#--------------------------------------------------
# Mixins
#--------------------------------------------------
class CriticalTaskMixin():
    pass

class PythonClass(CriticalTaskMixin, object):    
    def color(self):
        print('I am blue')
        
    def crititcal_task(self, extra=None):
        print('*** critical task ***')          # add method to base class

class SomeClass(PythonClass):
    def color(self):
        print('I am red')

class SomeOtherClass(PythonClass):
    def color(self):
        print('I am orange')

class NotFromPythonClass(object):           
    def color(self):
        print('I am yellow')

class NotFromPythonClassNoMethod(CriticalTaskMixin, object):    # inherit Mixin
    def color_1(self):                                          # different method name
        print('I am black')
    
    def crititcal_task(self, extra=None):               # not inherited
        print('### critical task  in black ###') 
                        
        
a = PythonClass()
b = SomeClass()
c = SomeOtherClass()
d = NotFromPythonClass()
e = NotFromPythonClassNoMethod()

some_objects = [a, b, c, d, e, a]

for obj in some_objects:
    if hasattr(obj, 'color'):
        obj.color()                                   
    if hasattr(obj, 'crititcal_task'):
            obj.crititcal_task()


























  











