# function named choose_from_hist that takes a histogram as defined in Section 11.1 and returns a random value from the histogram, chosen with probability in proportion to frequency. For example, for this histogram:
import random
def histogram(s):
  d = dict()
  for c in s:
    if c not in d:
      d[c] = 1
    else:
      d[c] += 1
  return d

def choose_from_hist(hist):
  no_of_letters=sum(hist.values())
  choice=random.choice(hist.keys())
  freq=hist[choice]
  print(choice+': probability' +str(freq) +'/' +str(no_of_letters))

hist=histogram('nitheesh nambianchery')
print(choose_from_hist(hist))
