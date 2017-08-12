'''
Problem 3: Write a program to list all the files in the given directory along with their length and last modification time. The output should contain one line for each file containing filename, length and modification date separated by tabs.

Hint: see help for os.stat.'''
import os

def readDir(d):
    return (f for f in os.listdir(d)
            if os.path.isfile(f))


for f in readDir('.'):
    s = os.stat(f)
    print(f, s[6], s[8])
