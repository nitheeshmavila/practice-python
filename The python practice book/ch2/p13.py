'''
Problem 13: Write a function lensort to sort a list of strings based on length.

>>> lensort(['python', 'perl', 'java', 'c', 'haskell', 'ruby'])
['c', 'perl', 'java', 'ruby', 'python', 'haskell']'''

import operator

def lensort(l):
    lenDict = {}
    for string in l:
        lenDict[string] = lenDict.get(string, 0) + len(string)
    sortedList = sorted(lenDict.items(), 
                            key = operator.itemgetter(1))
    return [key for key,value in sortedList]

print(lensort(['python', 'perl', 'java', 'c', 'haskell','ruby'])) 
        
    
    
