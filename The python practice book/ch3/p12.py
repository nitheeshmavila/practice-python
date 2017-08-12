'''
Problem 12: Write a program mydoc.py to implement the functionality of pydoc. The program should take the module name as argument and print documentation for the module and each of the functions defined in that module.

$ python mydoc.py os
Help on module os:

DESCRIPTION

os - OS routines for Mac, NT, or Posix depending on what system we're on.
...

FUNCTIONS

getcwd()
    ...


hints:
-----

The dir function to get all entries of a module
The inspect.isfunction function can be used to test if given object is a function
x.__doc__ gives the docstring for x.
The __import__ function can be used to import a module by name


run this in python2
'''
import sys
import inspect

def pydoc(m):
    module = __import__(m)
    print('Help on module %s'%(m))
    print('DESCRIPTION')
    print('%s - %s'%(m, module.__doc__))
    print('FUNCTIONS')
    
    for item in dir(module):
        obj = getattr(module, item)
        if inspect.isfunction(obj):
           print(obj.__doc__)

def main():
    if len(sys.argv) == 2:
        module = sys.argv[1]
        pydoc(module)
    else:
        print('invalid syntax')
        print('usage : python3 p12.py <modulename>')

if __name__ == '__main__':
    main()
