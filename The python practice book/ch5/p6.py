'''
Problem 6: Write a function to compute the total number of lines of code, ignoring empty and comment lines, in all python files in the specified directory recursively.

'''
import sys
import os
count = 0
def readDir(d):
    return (os.path.join(d, f)
            for f in os.listdir(d))
def readLines(f):
    return (line for line in open(f) 
            if not line.startswith('#') if  line != '')            

def getCount(d):
     global count
     for p in readDir(d):
        if  os.path.isfile(p):
            if os.path.splitext(p)[-1].lower() == '.py':
                for line in readLines(p):
                    count += 1
        else:
            getCount(p)
     return count       

def main():
    print('Total no of lines inside the python files in the directory with excluding comment and blank lines %s : %d'%(sys.argv[1],getCount(sys.argv[1]))) 
    
if __name__ == '__main__':
    main()
