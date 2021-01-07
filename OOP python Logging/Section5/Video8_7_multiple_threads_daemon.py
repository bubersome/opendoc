'''
Created on May 20, 2019
@author: Burkhard A. Meier
'''





from threading import Thread
import threading
from time import sleep


class PythonClass(object):    
    def __init__(self, data=None):
        self.data = data                                # data attribute
 
    def print_data(self):                               # regular class method
        print(self.data)
        
    def method_in_a_thread(self):                       # method to be run in a thread
        print('Starting a long running task...\n')       
        for _ in range(5):
            print('processing...')
            sleep(1)
        print('Completed long running task...')
        
        
cls_instance =  PythonClass('some data')                # create class instance   

print(threading.enumerate())
# Create a new Thread, set the target to the method to be run in a thread
run_thread = Thread(target=cls_instance.method_in_a_thread)
print(run_thread.isDaemon()) 
run_thread.setDaemon(True)
print(run_thread.isDaemon()) 
run_thread.start() 


sleep(0.01)
print()
print(threading.enumerate())

cls_instance.print_data()                               # call method
cls_instance.print_data()                               # call method again
exit()

















