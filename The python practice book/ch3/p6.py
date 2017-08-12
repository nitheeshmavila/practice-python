'''
Problem 6: Write a program antihtml.py that takes a URL as argument, downloads the html from web and print it after stripping html tags.

$ python antihtml.py index.html
...
The Python interpreter is usually installed as /usr/local/bin/python on
those machines where it is available; putting /usr/local/bin in your
'''

import re
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
    return basename

def antihtml(htmlfile):
    fp = open('con.txt', 'w')
    for line in open(htmlfile):
        if not line.strip().startswith('<') and not line.strip().endswith('>'):
            no_tag = re.sub("<.*?>",'',line)
            fp.write(no_tag)

   
def main():
    htmlfile = wget(sys.argv[1])
    antihtml(htmlfile)

if __name__ == '__main__':
    main()
