'''
def main(filename):
    frequency = word_frequency(read_words(filename))
    for word, count in frequency.items():
        print word, count

if __name__ == "__main__":
    import sys
    main(sys.argv[1])


Problem 34: Improve the above program to print the words in the descending order of the number of occurrences.'''

import sys

filename = sys.argv[1]
def word_frequency(words):
    frequency = {}
    for w in words:
        frequency[w] = frequency.get(w, 0) + 1
    return frequency

def read_words(filename):
    return open(filename).read().split()
frequency = word_frequency(read_words(filename))

def f(key):
    return frequency[key]

for key in sorted(frequency.keys(),key=f,reverse=True):
    print(key, frequency[key])
