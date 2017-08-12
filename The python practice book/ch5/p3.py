'''Problem 3: Write a function findfiles that recursively descends the directory tree for the specified directory and generates paths of all the files in the tree.

'''
import os
import sys

def read_dir(d):
    ''' it is a generator fn. which on each iteration of the generator object gives a path'''
    for f in os.listdir(d):
        path = os.path.join(d,f)
        yield path

def get_dir(direct):
    for path in read_dir(direct):
        if os.path.isfile(path):
            print(path)
        else:
            get_dir(path)

def main():
    files = get_dir(sys.argv[1])

if __name__ == '__main__':
    main()
