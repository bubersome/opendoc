'''
Created on May 21, 2019
@author: Burkhard A. Meier
'''





from queue import Queue

class PythonClass(object):    
    def __init__(self, data=None):
        self.data = data                                # data attribute
        self.use_queues()
 
    def print_data(self):                               # regular class method
        print(self.data)
            
    def use_queues(self):                               # Create Queue instance 
        gui_queue = Queue() 
        print(gui_queue)
             
        
cls_instance = PythonClass('some data')                # create class instance   
cls_instance.print_data()                               # call method












