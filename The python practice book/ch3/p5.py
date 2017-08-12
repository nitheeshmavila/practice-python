'''
Problem 5: Write a program wget.py to download a given URL. The program should accept a URL as argument, download it and save it with the basename of the URL. If the URL ends with a /, consider the basename as index.html.

$ python wget.py http://docs.python.org/tutorial/interpreter.html
saving http://docs.python.org/tutorial/interpreter.html as interpreter.html.

$ python wget.py http://docs.python.org/tutorial/
saving http://docs.python.org/tutorial/ as index.html.
'''
import sys
import urllib.request

def wget(url):
    if url.strip().endswith('/'):
        basename = 'index.html'
    else:
        basename = url.split('/')[-1]
    fout = open(basename, 'w')
    response = urllib.request.urlopen(url)
    print('Saving %s as %s'%(url, basename))
    for line in response:
        fout.write(line.decode("utf-8"))

def main():
    wget(sys.argv[1])

if __name__ == '__main__':
    main()

