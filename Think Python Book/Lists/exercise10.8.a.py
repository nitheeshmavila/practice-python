'''
Exercise 10.8
--------------
simple way to check if two words are anagram
'''
def is_anagram(a,b):
    print(sorted(a)==sorted(b))

is_anagram('nitheesh','nieeshth')
