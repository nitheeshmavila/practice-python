'''
Problem 16: Write a function extsort to sort a list of files based on extension.

>>> extsort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c'])
['a.c', 'x.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt']
'''
import operator

def extSort(l):
    fileDict = {}
    for filename in l:
        ext = filename.split('.')
        fileDict[filename] = fileDict.get(filename, '') + ext[1]
    sortedList = sorted(fileDict.items(),
                       key = operator.itemgetter(1))
    return [ key for key,value in sortedList]

print(extSort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c']))
    


