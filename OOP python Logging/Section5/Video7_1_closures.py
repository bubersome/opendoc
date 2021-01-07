'''
Created on May 17, 2019
@author: Burkhard A. Meier
'''






#------------------------------------------------------------
# closures - nested functions that enclose their surroundings
#------------------------------------------------------------

def not_a_closure(color='blue'):
    color_ready = color
    
    def inner_function():           # nested, inner function
        print(color_ready)
    
    inner_function()

not_a_closure()

#--------------------------------------------------

def a_closure(color='blue'):
    color_ready = color
    
    def inner_function():
        print(color_ready)
    
    return inner_function       # return function name, don't call it. No: ()

func = a_closure()              # func now is a reference to inner_function + the color_ready variable state
func()                          # invoke the inner function

#--------------------------------------------------





