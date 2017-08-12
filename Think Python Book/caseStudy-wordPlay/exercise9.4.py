'''
Exercise9.4
------------
Write a function named uses_only that takes a word and a string of letters, and that
returns True if the word contains only letters in the list. Can you make a sentence using
only the letters acefhlo ? Other than “Hoe alfalfa?”'''

def usesOnly(word, letters):
    for ch in word:
        if ch not in letters:
            return False
    return True

letters = input('enter letters string\n')
words = open('words.txt', 'r')
count = 0
for word in words:
        word = word.strip()
        if (usesOnly(word, letters)):
            print(word)
            count = count + 1
print("%d word contains only letters in %s"%(count, letters))
