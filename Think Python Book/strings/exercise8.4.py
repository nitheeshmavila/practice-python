'''
Exercise 8.4.
-------------
 Modify find so that it has a third parameter, the index in word where it should start looking.


'''

def find(word, letter, index):
    while index < len(word):
        if word[index] == letter:
            return '%s found in %s at index %d'%(letter, word, index)
        index += 1
    return '%s not found in %s'%(letter, word)    

print(find('nitheesh','e',1))
