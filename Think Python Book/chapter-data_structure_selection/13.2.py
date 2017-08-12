
#go to Project Gutenberg ( http: // gutenberg. org ) and download your favorite out-of-copyright book in plain text format.

#Modify your program from the previous exercise to read the book you downloaded, skip over the header information at the beginning of the file, and process the rest of the words as before.

#Then modify the program to count the total number of words in the book, and the number of times each word is used.

#Print the number of different words used in the book. Compare different books by different authors,written in different eras. Which author uses the most extensive vocabulary? 
from string import whitespace,digits,punctuation
books={'origin.txt','huck.txt', 'frank.txt','great.txt','meta.txt', 'sherlock.txt','tale.txt'}
def get_words(book):
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

def word_clean(word):
  word = word.strip(punctuation + whitespace + digits).lower()
  return(word)

def histogram(word_list):
  hist={}
  for word in word_list:
    hist[word]=hist.get(word,0)+1
    
  return(hist)

def books_info(books):
  words_list=[]
  unique={}#this dict stores book_name as key and unique words as keys
  for book in books:
    book_name=book
    book=open(book,'r')
    words_list=[word_clean(word) for word in get_words(book)] 
    book.close()
    print('%s has a total of %d words and %d unique words'%(book_name,len(words_list),len(histogram(words_list))))
    unique[book_name]=unique.get(book_name,0)+len(histogram(words_list))
  l=[key for key,value in sorted(unique.items(),reverse=True)]
  print("The author of the book %s has the most extensive vocabulary"%(l[0]))
books_info(books)
    
