import os

def read_dir(d):
    for f in os.listdir(d):
        path = os.path.join(d,f)
        yield path

def get_dir(direct):
    for path in read_dir(direct):
        if os.path.isfile(path):
            print path
        else:
            get_dir(path)

def main(directory):
    files = get_dir(directory)

cwd = os.getcwd()
#print cwd

main("/home/nitheesh/vs2016")
