'''
Exercise 10-10
---------------
Write a function that reads the file words.txt and builds a list with one element per
word. Write two versions of this function, one using the append method and the other
using the idiom t = t + [x] . Which one takes longer to run? Why?
Hint: use the time module to measure elapsed time.'''

import time

def buildList1(filename):
    words = open(filename)
    return [word.strip() for word in words]


def buildList2(filename):
    words = open(filename)
    l = []
    for word in words:
        word = word.strip()
        l.append(word)
    return l

def buildList3(filename):
    words = open(filename)
    l = []
    for word in words:
        word = word.strip()
        l += [word]
    return l

start = time.time()
#buildList1('words.txt')
#buildList2('words.txt')
buildList3('words.txt')

end = time.time()
elapsed = end - start
print(elapsed)

