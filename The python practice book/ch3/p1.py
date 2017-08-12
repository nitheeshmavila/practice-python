'''
Problem 1: Write a program to list all files in the given directory.'''

import os
 
def listFiles(d):
    ''' this fn list all files in the directory  d'''
    return os.listdir(d)



print(listFiles(input()))





