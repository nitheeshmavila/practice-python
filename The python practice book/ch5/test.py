
''' Write a fn to compute the number of python files (.py extension) in a 
specified directory recursively. '''

import os
count = 0

def extract(direct):
    for path in os.listdir(direct):
        path = os.path.join(direct,path)
        yield path

def main(directory):
    global count
    
    for path in extract(directory):
        if os.path.isfile(path):
            ext = path.split('.')
            if ext[-1] == 'py':
                count += 1
            else :
                pass
        else :  
            main(path)
    
    print "No.of python files found : %d" % (count)

directory = "/home/nitheesh/vs2016"
main(directory)
