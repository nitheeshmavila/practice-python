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

def no_of_words(hist):
  return sum(hist.values())

def no_of_different_words(hist):
  return len(hist)


hist=process_file('a.txt')
print(no_of_words(hist))
print(no_of_different_words(hist))
