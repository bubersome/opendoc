'''
Created on Jun 20, 2019
@author: Burkhard A. Meier
'''









class PythonSuperClass():
    def __init__(self, name, items):
        self.name = name
        self.items = items
        
    def get_name_and_items(self):   
        return self.name, self.items  
    
    def __repr__( self ):
        return f'PythonSuperClass({self.name}, {self.items})'    
    
        
class PythonClass(PythonSuperClass):
    def __init__(self, name, items=None):
        super().__init__(name, items)         

    def __str__(self):
        return "{name}, {items}".format(**self.__dict__)

    def __repr__( self ):
        return f'PythonClass({self.name}, {self.items})'


if __name__ == "__main__":
    # args: PythonClass  Bob  Spaceship  
    # args: PythonSuperClass Space 1
    
    import sys
    args = sys.argv
    num_of_args = len(args)
    print()
    print("Number of arguments: ", num_of_args)
    print(args[1:])
    print("Name of script:", args[0].split('\\')[-1])
    
    
    if "PythonClass" in args and num_of_args >= 2:
        args.remove("PythonClass")
        print(args[1:])
        if num_of_args == 2:
            obj = PythonClass(name=args[1])
            print(obj)
            print(repr(obj))
        elif num_of_args > 2:
            obj = PythonClass(name=args[1], items=args[2])
            print(obj)
            print(repr(obj))    
    

    if "PythonSuperClass" in args and num_of_args >= 3:
        args.remove("PythonSuperClass")
        print(args[1:])
        if num_of_args > 3:
            obj = PythonClass(name=args[1], items=args[2])
            print(obj)
            print(repr(obj))  
    
 
 


























