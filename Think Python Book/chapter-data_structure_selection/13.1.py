#Exercise 13.1. Write a program that reads a file, breaks each line into words, strips whitespace and punctuation from the words, and converts them to lowercase.
from  string import punctuation,whitespace,digits
book='think_python.txt'
f=open(book,'r')
words=f.read().split()
    
def word_clean(word):
   word = word.strip(punctuation + whitespace + digits).lower()
   return(word)

print( "The book {} has {} 'words'".format(book,len([word_clean(word) for word in words ])))
