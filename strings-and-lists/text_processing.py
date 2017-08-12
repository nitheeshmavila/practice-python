#Exercise 13.1. Write a program that reads a file, breaks each line into words, strips whitespace and punctuation from the words, and converts them to lowercase.
from  string import punctuation,whitespace,digits
def converts(filename):
  f=open(filename,'r')
  contents=f.read()
  words=contents.split()
  text=''
  for word in words:
    word = word.strip(punctuation + whitespace + digits)
    word = word.lower()
    text=text+' '+word
    print(text)
    
