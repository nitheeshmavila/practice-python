#Modify the previous program to read a word list (see Section 9.1) and then
# print all the words in the book that are not in the word list. How many of
# them are typos? How many of them are common words that should be in the word
# list, and how many of them are really obscure?

from string import punctuation, whitespace
books = ['origin.txt', 'huck.txt', 'great.txt', 'meta.txt', 'sherlock.txt', 'frank.txt', 'tale.txt']

def words(book):
    list_ = []
    flag = False
    signal = "*** START OF"
    for line in book:
        if flag == True:
            for word in line.split():
                list_.append(word)
        elif (signal in line) and (flag == False):
            flag = True
        else:
            pass
    return list_
    
def clean(word):
    result = ''
    for char in word:
        if (char in whitespace) or (char in punctuation):
            pass
        elif not char.isalpha():
            pass
        else:
            result += char.lower()
    return result

def stats():
    for book in books:
        book_words = set([clean(word) for word in words(open(book, 'r'))])
        words_ = set([word for word in open(word_file, 'r')])
        print "Stats for %s" % open(book, 'r').name
        print "  There are %s non-listed words." % len(book_words - words_)
        
stats()

print "\n\nThe words not in the word list for origin.txt:"
print set([clean(word) for word in words(open(origin, 'r'))]) - \
      set([word for word in open(word_file, 'r')])
