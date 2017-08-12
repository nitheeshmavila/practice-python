'''
Problem 2: Write a program extcount.py to count number of files for each extension in the given directory. The program should take a directory name as argument and print count and extension for each available file extension.

$ python extcount.py src/
14 py
4 txt'''

import os
import sys

def readDir(d):
   return (f for f in os.listdir(d) 
            if os.path.isfile(f))
    

def countExn(d):
    print(d)
    extnDict = {}
    for f in readDir(d):
        key =  os.path.splitext(f)[-1].strip('.')
        extnDict[key] = extnDict.get(key, 0) + 1
    return extnDict

def main():
    dic = countExn(sys.argv[1])
    for key in dic:
        print(dic[key], key)
    
if __name__ == '__main__':
    main()
    
   
  
      
