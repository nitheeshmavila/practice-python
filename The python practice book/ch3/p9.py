'''
Problem 9: Write a regular expression to validate a phone number'''

import re

def validatePhone(number):
    numpat = r'^([+]?\d{1,2})?(\d{10})$'
    return  re.search(numpat, number)

def main():
    phonenumber = input()
    if validatePhone(phonenumber):
        print('%s is a valide mobile number'%(phonenumber))
    else:
        print('%s is not a valide mobile number'%(phonenumber))

if __name__=='__main__':
    main() 
