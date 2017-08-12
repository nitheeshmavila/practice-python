def readLines(f):
    return (line for line in open(f) 
            if not line.startswith('#') if  line != '')            

def getCount(d):
     global count
     for p in readDir(d):
        if  os.path.isfile(p):
            if os.path.splitext(p)[-1].lower() == '.py':
                for line in readLines(p):
