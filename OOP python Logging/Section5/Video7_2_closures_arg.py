'''
Created on May 17, 2019
@author: Burkhard A. Meier
'''






#------------------------------------------------------------
# closures - nested functions that enclose their surroundings
#------------------------------------------------------------


def a_closure(color='blue'):
    color_ready = color
    
    def inner_function(data):                       # now requires an argument
        print(f'Closure: {data} {color_ready}')
    
    return inner_function           # return function name, don't call it. No: ()
#---------------------------

func = a_closure()                  # func now is a reference to inner_function + the color_ready variable state
arg = 1
func(arg)                           # invoke the inner function, pass in arg



















