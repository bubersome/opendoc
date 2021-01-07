'''
Created on May 21, 2019
@author: Burkhard A. Meier
'''




from threading import Thread
from queue import Queue
from time import sleep
import Section5.Video9_6_queue_module as queue_module

class PythonClass(object):    
    def __init__(self, data=None):
        self.data = data                                # data attribute
        self.gui_queue = Queue()                        # create queue instance variable
#         self.create_thread()
        queue_module.write_to_queue(self)               # pass in self/instance to imported function

    def use_queues(self):                               # Now using a class instance queue        
        while True: 
            print(self.gui_queue.get())
                   
    def create_thread(self):
        write_thread = Thread(target=self.use_queues)       # start queue in its own thread
        write_thread.setDaemon(True)                        # run as background thread
        write_thread.start() 
 
    def print_data(self):                                   # regular class method
        print(self.data)
            
if __name__== '__main__':        
    cls_instance =  PythonClass('*** some data\n')          # create class instance   
    cls_instance.print_data()                               # call method
    
    cls_inst_1 = PythonClass('***different data')           # create another class instance 
    sleep(0.1)
    cls_inst_1.print_data()                                 # call method on other instance












