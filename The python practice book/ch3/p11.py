'''
Problem 11: Write a python program zip.py to create a zip file. The program should take name of zip file as first argument and files to add as rest of the arguments.
$ python zip.py foo.zip file1.txt file2.txt
'''
import sys
import zipfile

def main():
    if len(sys.argv) > 2 :
        z = zipfile.ZipFile(sys.argv[1], 'w')
        files = sys.argv[2:]
        for f in files:
            z.write(f)
        z.close()
    else:
        print('invalid usage')
        print("usage: python3 p11.py 'zipfilename' 'file1' 'file2' ....'filen'")

if __name__ == '__main__':
    main()
        
    
