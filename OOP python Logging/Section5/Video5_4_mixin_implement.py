'''
Created on May 17, 2019
@author: Burkhard A. Meier
'''





#--------------------------------------------------
# Mixins
#--------------------------------------------------
from datetime import datetime
from time import sleep

class Mixin():
    def log_critical(self, extra=None):
            print(datetime.now(), extra)
            sleep(0.2)
            start = datetime.now()
            print(start, "... processing ...")
            sleep(0.5)
            finish = datetime.now()
            print(finish, "... completed.")
            print(f"Runtime: {finish - start} \n")
            

class PythonClass(Mixin, object):    
    def color(self):
        print('I am blue')
        
    def crititcal_task(self, extra=None):
        Mixin().log_critical(f'... Critical task started in: ' + self.__class__.__qualname__)          

class SomeClass(PythonClass):
    def color(self):
        print('I am red')

class SomeOtherClass(PythonClass):
    def color(self):
        print('I am orange')

class NotFromPythonClass(object):           
    def color(self):
        print('I am yellow')

class NotFromPythonClassNoMethod(Mixin, object):    # inherit Mixin
    def color_1(self):                                          # different method name
        print('I am black')
    
    def crititcal_task(self, extra=None):               # not inherited
        Mixin().log_critical(f'... Critical task started in: ' + self.__class__.__qualname__)  
                        
        
a = PythonClass()
b = SomeClass()
c = SomeOtherClass()
d = NotFromPythonClass()
e = NotFromPythonClassNoMethod()

some_objects = [a, b, c, d, e, a]

for obj in some_objects:                              
    if hasattr(obj, 'crititcal_task'):
            obj.crititcal_task()


























  











