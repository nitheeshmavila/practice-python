'''
Problem 7: Write a program split.py, that takes an integer n and a filename as command line arguments and splits the file into multiple small files with each having n lines'''

import sys
import os

def getlines(filename):
   return (line for line in open(filename))

def split(filename,n):
    i = 1
    count = 0
    fp = open('sub0'+os.path.splitext(filename)[1],'w')
    for line in getlines(filename):
        if count == n:
            fp.close()
            fp = open('sub' + str(i) + os.path.splitext(filename)[1],'w')
            count = 0
            i += 1
        fp.write(line)
        count += 1
    fp.close()

if len(sys.argv) != 3:
    print ('usage : python split.py <n> <filename>')
else:
    split(sys.argv[2],int(sys.argv[1]))
