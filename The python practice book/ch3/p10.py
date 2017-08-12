'''
Problem 10: Write a program myip.py to print the external IP address of the machine. Use the response from http://httpbin.org/get and read the IP address from there. The program should print only the IP address and nothing else.

run this in python2
'''
import urllib
import  json

def myip(url):
    data = json.loads(urllib.urlopen(url).read())
    print data['origin']

def main():
    myip('http://httpbin.org/get')

if __name__ == '__main__':
    main()
