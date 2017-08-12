'''
Problem 6: Write a function to compute the total number of lines of code, ignoring empty and comment lines, in all python files in the specified directory recursively.

'''
import sys
import os
count = 0
def readDir(d):
    return (os.path.join(d, f)
            for f in os.listdir(d))
