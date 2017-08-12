'''
Exercise 9-2.
--------------
In 1939 Ernest Vincent Wright published a 50,000 word novel called Gadsby that does
not contain the letter “e.” Since “e” is the most common letter in English, that’s not easy
to do.
In fact, it is difficult to construct a solitary thought without using that most common
symbol. It is slow going at first, but with caution and hours of training you can gradually
gain facility.
All right, I’ll stop now.
Write a function called has_no_e that returns True if the given word doesn’t have the
letter “e” in it.
Modify your program from the previous section to print only the words that have no
“e” and compute the percentage of the words in the list have no “e.”'''


def hasNoE(word):
    for ch in word:
        if ch == 'e': 
            return False
    return True

#print(hasNoE('nitheesh'))
#print(hasNoE('mithun'))

def printWordsNoE(filename):
    words = open(filename, 'r')
    for word in words:
        if hasNoE(word):
            print(word)

#printWordsNoE('words.txt')

def percentageWords(filename):
    #  compute the percentage of the words in the file have no “e.”
    words = open(filename, 'r')
    totalWords = 0
    haveNoEWords = 0
    for word in words:
        totalWords += 1
        if hasNoE(word):
            haveNoEWords += 1
    print("total words : %d \nno of words that has no 'e': %d"%( totalWords,haveNoEWords))
    per = (haveNoEWords / totalWords) * 100
    return 'percentage:%d'%(per)


    
print(percentageWords('words.txt'))
