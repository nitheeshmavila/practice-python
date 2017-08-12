#Exercise 13.3. Modify the program from the previous exercise to print the 20 most frequently-used words in the book.
from string import digits,punctuation,whitespace
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

 
def most_common_words(hist): 
  wordlist=[(value,key) for key,value in hist.items()]
  wordlist.sort(reverse=True)
  for freq,word in wordlist[:20]:
    print(word)
  return(wordlist)

def books_info(books):
  words_list=[]
  unique={}#this dict stores book_name as key and unique words as keys
  for book in books:
    book_name=book
    book=open(book,'r')
    words_list=[word_clean(word) for word in get_words(book)] 
    book.close()
    print('%s has a total of %d words and %d unique words'%(book_name,len(words_list),len(histogram(words_list))))
    print('The most common 20 words are \n')
    most_common_words(histogram(words_list))
    unique[book_name]=unique.get(book_name,0)+len(histogram(words_list))
  l=[key for key,value in sorted(unique.items(),reverse=True)]
  print("The author of the book %s has the most extensive vocabulary"%(l[0]))
books_info(books)
    

