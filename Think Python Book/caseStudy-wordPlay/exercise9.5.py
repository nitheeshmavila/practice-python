'''
Exercise 9-5.
---------------
Write a function named uses_all that takes a word and a string of required letters, and
that returns True if the word uses all the required letters at least once. How many words
are there that use all the vowels aeiou ? How about aeiouy'''

def usesAll(word, letters):
    for l in letters:
        if l not in word:
            return False
    return True

words = open('words.txt','r')
count = 0
letters = 'aeiou'
for word in words:
    if usesAll(word, letters):
         print(word)
         count += 1
print('%d words uses all the letters in %s at least once'%(count, letters)) 







