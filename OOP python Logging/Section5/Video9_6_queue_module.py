'''
Created on May 20, 2019
@author: Burkhard A. Meier
'''







def write_to_queue(inst):
    print('hi from Queue', inst)
    if hasattr(inst, 'gui_queue'):
        for idx in range(10): 
            inst.gui_queue.put('Message from a queue: ' + str(idx)) 
        inst.create_thread()
    
















