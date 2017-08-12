#Python provides a data structure called set that provides many common set opera-tions. Read the documentation at http: // docs. python. org/ 2/ library/ stdtypes. html# types-set and write a program that uses set subtraction to find words in the book that are not in the word list.
import string
def process_file(filename):
  hist = dict()
  fp = open(filename)
  for line in fp:
    process_line(line, hist)
  return hist

def process_line(line, hist):
  line = line.replace('-', ' ')
  for word in line.split():
    word = word.strip(string.digits+string.punctuation + string.whitespace)
    word = word.lower()
    hist[word] = hist.get(word, 0) + 1
  return(hist)


def set_difference(hist,wordlist):# wordlist is a set 
  words=[(value,key) for key,value in hist.items()]
  words=set(words)
  difference=words-wordlist
  return(difference)


hist=process_file('think_python.txt')
print(set_difference(hist,{'the','me','where','out','there','what','get'}))


