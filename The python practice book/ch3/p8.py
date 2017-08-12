'''
Problem 8: Write a program links.py that takes URL of a webpage as argument and prints all the URLs linked from that webpage.'''

import re
import sys
import urllib.request

def printurls(url):
    page = urllib.request.urlopen(url)
    link = r'https?://.+?"'
    for line in page:
        line = line.decode("utf-8")
        l = re.findall(link, line)
        if l:
            print(l[0])

def main():
    printurls(sys.argv[1])

if __name__ == '__main__':
    main()

