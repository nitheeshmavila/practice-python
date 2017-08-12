'''
Problem 2: Write a program that takes one or more filenames as arguments and prints all the lines which are longer than 40 characters.'''

import sys

def readFiles(filename):
    ''' this function returns a generator object where each line is longer than 40 characters'''
    return (line for f in filename 
             for line in open(f)
             if len(line) > 40)
def main():
    lines = readFiles(sys.argv[1:])
    for line in lines:
        print(line)

if __name__ == '__main__':
    main()

