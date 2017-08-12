'''
Exercise 11-2.
---------------
Dictionaries have a method called get that takes a key and a default value. If the key
appears in the dictionary, get returns the corresponding value; otherwise it returns the
default value.'''

def createDict(filename):
    wordDict = {}
    words = open(filename)
    for word in words:
        word = word.strip()
        wordDict[word] = wordDict.get(word, 0) + 1
    return wordDict


