'''Problem 4: Write a function to compute the number of python files (.py extension) in a specified directory recursively.'''
import sys
import os
count = 0
def readDir(d):
    return (os.path.join(d, f)
            for f in os.listdir(d))
            
def getCount(d):
     global count
     for p in readDir(d):
        if  os.path.isfile(p):
            if os.path.splitext(p)[-1].lower() == '.py':
                count += 1
        else:
            getCount(p)
     return count       

print('Total python files:',getCount('/home/nitheesh/vs2016'))
