'''
Exercise 11.1
-------------
Write a function that reads the words in words.txt and stores them as keys in a dic
tionary. It doesn’t matter what the values are. Then you can use the in operator as a fast
way to check whether a string is in the dictionary.'''

def createDict(filename):
    wordDict = {}
    words = open(filename)
    for word in words:
        word = word.strip()
        wordDict[word] = wordDict.get(word, 0) + 1
    return wordDict

d = createDict('words.txt')
for word in d:
    if word == 'top':
        print('yes')
