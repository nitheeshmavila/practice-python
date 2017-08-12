'''
Problem 35: Write a program to count frequency of characters in a given file. Can you use character frequency to tell whether the given file is a Python program file, C program file or a text file?'''

from string import ascii_lowercase     # ascii_lowercase =='abcdefghijklmnopqrstuvwxyz'
with open('java.txt') as f:
    text = f.read().strip()
    dic = {}
    for x in ascii_lowercase:
        dic[x] = text.count(x)
print(dic)
