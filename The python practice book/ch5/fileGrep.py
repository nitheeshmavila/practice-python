'''
given a list of files, you need to print the lines it has a particular pattern'''

def readFiles(filenames):
   return (line for f in filenames
            for line in open(f))
            

def grep(lines, pattern):
   return (line for line in lines
           if pattern in line)
            

def printLines(patternLines):
    for line in patternLines:
        print(line)

def main():
    filenames = ['1.txt', '2.txt', '3.txt']
    pattern = 'Unix'
    lines = readFiles(filenames)
    patternLines  = grep(lines, pattern)
    printLines(patternLines)

if __name__=='__main__':
    main()
