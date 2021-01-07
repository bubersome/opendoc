'''
Created on May 20, 2019
@author: Burkhard A. Meier
'''





from threading import Thread

class PythonClass(object):    
    def __init__(self, data=None):
        self.data = data                                # data attribute
 
    def print_data(self):                               # regular class method
        print(self.data)
        
    def method_in_a_thread(self):                       # method to be run in a thread
        print('Hi, I am a long running task...')       
        
        
cls_instance =  PythonClass('some data')                # create class instance   
cls_instance.print_data()                               # call method

# Create a new Thread, set the target to the method to be run in a thread
run_thread = Thread(target=cls_instance.method_in_a_thread)
run_thread.start()  




















